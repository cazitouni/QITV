from qgis.core import (
    Qgis,
    QgsCategorizedSymbolRenderer,
    QgsFeature,
    QgsField,
    QgsFields,
    QgsGeometry,
    QgsLineSymbol,
    QgsManhattanLineCallout,
    QgsMarkerSymbol,
    QgsPalLayerSettings,
    QgsProject,
    QgsRendererCategory,
    QgsSimpleLineSymbolLayer,
    QgsTask,
    QgsTextBufferSettings,
    QgsTextFormat,
    QgsVectorLayer,
    QgsVectorLayerSimpleLabeling,
)
from qgis.PyQt.QtCore import QVariant
from qgis.PyQt.QtGui import QColor, QFont


class ProcessingTask(QgsTask):
    def __init__(self, description, filename, content, layer_id, selected_field):
        super().__init__(description)
        self.filename = filename
        self.content = content
        self.layer_id = layer_id
        self.selected_field = selected_field
        self.result_text = ""
        self.error = None

    def run(self):
        try:
            project = QgsProject.instance()
            layer = project.mapLayer(self.layer_id)
            if not layer:
                self.result_text = "La couche sélectionnée est absente"
                return True
            idx = layer.fields().indexFromName(self.selected_field)
            if idx == -1:
                self.result_text = (
                    f"La couche sélectionée de dispose pas d'attributs "
                    f"'{self.selected_field}'."
                )
                return True
            nr_troncon_geom_map = {}
            for feat in layer.getFeatures():
                nr_value = feat.attribute(self.selected_field)
                if nr_value is not None:
                    nr_troncon_geom_map[str(nr_value)] = feat.geometry()
            if not nr_troncon_geom_map:
                self.result_text = "Pas de géométries valides dans la couche."
                return True
            all_line_fields = set()
            all_obs_fields = set()
            unique_observations = set()
            obs_count_per_troncon = {}
            for elem in self.content:
                for key, _ in elem.items():
                    if key != "observation":
                        all_line_fields.add(key)
                numero_troncon = elem.get("numero_troncon")
                if numero_troncon and numero_troncon in nr_troncon_geom_map:
                    observations = elem.get("observations", [])
                    valid_obs_count = 0
                    for obs in observations:
                        all_obs_fields.update(obs.keys())
                        unique_observations.add(obs.get("observation", ""))
                        emplacement_long = obs.get("emplacement_longitudinal")
                        if emplacement_long is not None and emplacement_long != "":
                            try:
                                dist = float(emplacement_long)
                                geom = nr_troncon_geom_map[numero_troncon]
                                if geom.length() >= dist:
                                    valid_obs_count += 1
                            except ValueError:
                                pass
                    obs_count_per_troncon[numero_troncon] = valid_obs_count
            mem_layer = self._create_observation_layer(layer, all_obs_fields)
            line_layer = self._create_line_layer(layer, all_line_fields)
            point_features = []
            line_features = []
            results = []
            for elem in self.content:
                numero_troncon = elem.get("numero_troncon")
                if not numero_troncon:
                    results.append(f"Information absente 'numero_troncon': {elem}")
                    continue
                geom = nr_troncon_geom_map.get(numero_troncon)
                if not geom:
                    results.append(
                        f"Pas de géométrie pour le troncon: {numero_troncon}"
                    )
                    continue
                line_geom = self._process_line_geometry(
                    geom, elem.get("sens_ecoulement", "")
                )
                line_feat = self._create_line_feature(
                    elem,
                    geom,
                    obs_count_per_troncon.get(numero_troncon, 0),
                    line_layer.fields(),
                    all_line_fields,
                )
                line_features.append(line_feat)
                observations = elem.get("observations", [])
                count_added = 0
                for obs in observations:
                    point_feat = self._create_point_feature(
                        obs, line_geom, elem, mem_layer.fields(), all_obs_fields
                    )
                    if point_feat:
                        point_features.append(point_feat)
                        count_added += 1
                results.append(
                    f"Troncon: {numero_troncon} - {count_added} observations ajoutées"
                )
            if line_features:
                line_layer.dataProvider().addFeatures(line_features)
            if point_features:
                mem_layer.dataProvider().addFeatures(point_features)
            line_layer.updateExtents()
            mem_layer.updateExtents()
            project.addMapLayer(line_layer)
            project.addMapLayer(mem_layer)
            self._apply_line_styling(line_layer)
            self._apply_point_styling(mem_layer, unique_observations)
            self._apply_labeling(mem_layer)
            self.result_text = (
                "\n".join(results)
                if results
                else "Pas de géométries ou d'observations trouvées"
            )
            return True
        except Exception as e:
            self.error = e
            return True

    def _create_observation_layer(self, source_layer, obs_fields):
        """Create point layer with ALL observation fields"""
        crs_string = "Point?crs=" + source_layer.crs().authid()
        mem_layer = QgsVectorLayer(crs_string, "Observation", "memory")
        fields = QgsFields()
        for field_name in sorted(obs_fields):
            if field_name == "emplacement_longitudinal":
                fields.append(QgsField(field_name, QVariant.Double))
            else:
                fields.append(QgsField(field_name, QVariant.String))
        mem_layer.dataProvider().addAttributes(fields)
        mem_layer.updateFields()
        return mem_layer

    def _create_line_layer(self, source_layer, line_fields):
        """Create line layer with ALL line fields"""
        crs_string = "LineString?crs=" + source_layer.crs().authid()
        line_layer = QgsVectorLayer(crs_string, "Inspection", "memory")
        fields = QgsFields()
        fields.append(QgsField("observation_count", QVariant.Int))
        for field_name in sorted(line_fields):
            if field_name in [
                "etendue_inspection_prevue",
                "profondeur_noeud_depart",
                "profondeur_noeud_arrivee",
            ]:
                fields.append(QgsField(field_name, QVariant.Double))
            elif field_name in ["hauteur", "largeur"]:
                fields.append(QgsField(field_name, QVariant.Int))
            else:
                fields.append(QgsField(field_name, QVariant.String))
        line_layer.dataProvider().addAttributes(fields)
        line_layer.updateFields()
        return line_layer

    def _process_line_geometry(self, geom, sens_ecoulement):
        """Process line geometry based on flow direction"""
        if "amont" not in sens_ecoulement.lower():
            return geom
        if geom.isMultipart():
            lines = geom.asMultiPolyline()
            reversed_lines = [list(reversed(line)) for line in lines]
            return QgsGeometry.fromMultiPolylineXY(reversed_lines)
        else:
            line = geom.asPolyline()
            return QgsGeometry.fromPolylineXY(list(reversed(line)))

    def _create_point_feature(self, obs, line_geom, parent_elem, fields, obs_fields):
        """Create point feature with ALL observation and parent data"""
        emplacement_long = obs.get("emplacement_longitudinal")
        if emplacement_long is None or emplacement_long == "":
            return None
        try:
            dist = float(emplacement_long)
        except ValueError:
            return None
        if line_geom.length() < dist:
            return None
        point_geom = line_geom.interpolate(dist)
        if point_geom.isEmpty():
            return None
        feat = QgsFeature()
        feat.setGeometry(point_geom)
        feat.setFields(fields)
        for field_name in obs_fields:
            value = obs.get(field_name)
            if value is not None:
                if field_name == "emplacement_longitudinal":
                    feat[field_name] = float(value) if value != "" else None
                else:
                    feat[field_name] = str(value) if value != "" else None
            else:
                feat[field_name] = None
        return feat

    def _create_line_feature(self, elem, geom, obs_count, fields, line_fields):
        """Create line feature with ALL line data"""
        feat = QgsFeature()
        feat.setGeometry(geom)
        feat.setFields(fields)
        feat["observation_count"] = obs_count
        for field_name in line_fields:
            value = elem.get(field_name)
            if value is not None:
                if field_name in [
                    "etendue_inspection_prevue",
                    "profondeur_noeud_depart",
                    "profondeur_noeud_arrivee",
                ]:
                    try:
                        feat[field_name] = float(value) if value != "" else None
                    except (ValueError, TypeError):
                        feat[field_name] = None
                elif field_name in ["hauteur", "largeur"]:
                    try:
                        feat[field_name] = int(value) if value != "" else None
                    except (ValueError, TypeError):
                        feat[field_name] = None
                else:
                    feat[field_name] = str(value) if value != "" else None
            else:
                feat[field_name] = None
        return feat

    def _apply_line_styling(self, line_layer):
        """Apply double line styling"""
        symbol = QgsLineSymbol()
        left_line = QgsSimpleLineSymbolLayer.create(
            {
                "color": "blue",
                "width": "0.5",
                "offset": "-1.5",
            }
        )
        right_line = QgsSimpleLineSymbolLayer.create(
            {
                "color": "blue",
                "width": "0.5",
                "offset": "1.5",
            }
        )
        symbol.deleteSymbolLayer(0)
        symbol.appendSymbolLayer(left_line)
        symbol.appendSymbolLayer(right_line)
        line_layer.renderer().setSymbol(symbol)
        line_layer.triggerRepaint()

    def _apply_point_styling(self, mem_layer, unique_observations):
        """Apply categorized styling based on observation types"""
        categories = []
        special_obs = {"Type du noeud de départ", "Référence du noeud d'arrivée"}
        for obs_val in unique_observations:
            if obs_val in special_obs:
                symbol = QgsMarkerSymbol.createSimple(
                    {"name": "cross2", "color": "black", "size": "3"}
                )
            else:
                symbol = QgsMarkerSymbol.createSimple(
                    {"name": "circle", "color": "gray", "size": "2"}
                )
            categories.append(QgsRendererCategory(obs_val, symbol, obs_val))
        renderer = QgsCategorizedSymbolRenderer("observation", categories)
        mem_layer.setRenderer(renderer)
        mem_layer.triggerRepaint()

    def _apply_labeling(self, mem_layer):
        """Apply HTML labeling with callouts"""
        label_settings = QgsPalLayerSettings()
        label_settings.fieldName = """
            '<b>' || coalesce("observation", '') || '</b>' ||
            CASE 
                WHEN coalesce("caracterisation_1", '') != '' OR 
                coalesce("caracterisation_2", '') != '' 
                THEN '<p><font size="2">' || coalesce("caracterisation_1", '') || 
                '</p>' ||
                    CASE WHEN coalesce("caracterisation_1", '') != '' 
                    AND coalesce("caracterisation_2", '') != '' 
                        THEN '<p>' ELSE '' END ||
                    coalesce("caracterisation_2", '') || '</font></p>'
                ELSE ''
            END
        """
        label_settings.isExpression = True
        label_settings.placement = Qgis.LabelPlacement.AroundPoint
        label_settings.placementFlags = Qgis.LabelPredefinedPointPosition.TopRight
        label_settings.dist = 10
        callout = QgsManhattanLineCallout()
        callout.setEnabled(True)
        line_symbol = QgsLineSymbol.createSimple({"color": "black", "width": "0.15"})
        callout.setLineSymbol(line_symbol)
        label_settings.setCallout(callout)
        text_format = QgsTextFormat()
        text_format.setFont(QFont("Arial", 10))
        text_format.setSize(10)
        text_format.setAllowHtmlFormatting(True)
        buffer_settings = QgsTextBufferSettings()
        buffer_settings.setEnabled(True)
        buffer_settings.setSize(1.2)
        buffer_settings.setColor(QColor("white"))
        text_format.setBuffer(buffer_settings)
        label_settings.setFormat(text_format)
        labeling = QgsVectorLayerSimpleLabeling(label_settings)
        mem_layer.setLabelsEnabled(True)
        mem_layer.setLabeling(labeling)
        mem_layer.triggerRepaint()
