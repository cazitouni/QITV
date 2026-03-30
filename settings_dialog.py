"""
settings_dialog.py
Plugin settings dialog — lets the user pick the tronçon and branchement
layers + ID fields, then saves everything to config.json.
"""

from qgis.core import QgsMapLayer, QgsProject, QgsWkbTypes
from qgis.PyQt.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QGroupBox,
    QMessageBox,
    QVBoxLayout,
)

from .config import load_config, save_config


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Paramètres QITV")
        self.resize(400, 280)
        layout = QVBoxLayout()
        grp_t = QGroupBox("Couche tronçon")
        form_t = QFormLayout()
        self.troncon_layer_combo = QComboBox()
        self.troncon_field_combo = QComboBox()
        form_t.addRow("Couche :", self.troncon_layer_combo)
        form_t.addRow("Champ identifiant :", self.troncon_field_combo)
        grp_t.setLayout(form_t)
        grp_b = QGroupBox("Couche branchement")
        form_b = QFormLayout()
        self.branch_layer_combo = QComboBox()
        self.branch_field_combo = QComboBox()
        form_b.addRow("Couche :", self.branch_layer_combo)
        form_b.addRow("Champ identifiant :", self.branch_field_combo)
        grp_b.setLayout(form_b)
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        layout.addWidget(grp_t)
        layout.addWidget(grp_b)
        layout.addWidget(self.button_box)
        self.setLayout(layout)
        self.troncon_layer_combo.currentIndexChanged.connect(
            self._populate_troncon_fields
        )
        self.branch_layer_combo.currentIndexChanged.connect(
            self._populate_branch_fields
        )
        self.button_box.accepted.connect(self._on_ok)
        self.button_box.rejected.connect(self.reject)
        self._populate_layers()
        self._restore_from_config()

    def _line_layers(self):
        """Return all line vector layers in the current project."""
        return [
            layer
            for layer in QgsProject.instance().mapLayers().values()
            if layer.type() == QgsMapLayer.VectorLayer
            and QgsWkbTypes.geometryType(layer.wkbType()) == QgsWkbTypes.LineGeometry
        ]

    def _populate_layers(self):
        self.troncon_layer_combo.clear()
        self.branch_layer_combo.clear()
        for layer in self._line_layers():
            self.troncon_layer_combo.addItem(layer.name(), layer.id())
            self.branch_layer_combo.addItem(layer.name(), layer.id())
        self._populate_troncon_fields()
        self._populate_branch_fields()

    def _populate_troncon_fields(self):
        self.troncon_field_combo.clear()
        layer = self._current_layer(self.troncon_layer_combo)
        if layer:
            for field in layer.fields():
                self.troncon_field_combo.addItem(field.name())

    def _populate_branch_fields(self):
        self.branch_field_combo.clear()
        layer = self._current_layer(self.branch_layer_combo)
        if layer:
            for field in layer.fields():
                self.branch_field_combo.addItem(field.name())

    def _current_layer(self, combo):
        layer_id = combo.currentData()
        if not layer_id:
            return None
        return QgsProject.instance().mapLayer(layer_id)

    def _restore_from_config(self):
        cfg = load_config()
        self._set_combo_by_data(
            self.troncon_layer_combo, cfg.get("troncon_layer_id", "")
        )
        self._populate_troncon_fields()
        self._set_combo_by_text(self.troncon_field_combo, cfg.get("troncon_field", ""))
        self._set_combo_by_data(
            self.branch_layer_combo, cfg.get("branchement_layer_id", "")
        )
        self._populate_branch_fields()
        self._set_combo_by_text(
            self.branch_field_combo, cfg.get("branchement_field", "")
        )

    @staticmethod
    def _set_combo_by_data(combo, value):
        for i in range(combo.count()):
            if combo.itemData(i) == value:
                combo.setCurrentIndex(i)
                return

    @staticmethod
    def _set_combo_by_text(combo, value):
        idx = combo.findText(value)
        if idx >= 0:
            combo.setCurrentIndex(idx)

    def _on_ok(self):
        troncon_layer_id = self.troncon_layer_combo.currentData() or ""
        troncon_field = self.troncon_field_combo.currentText().strip()
        branch_layer_id = self.branch_layer_combo.currentData() or ""
        branch_field = self.branch_field_combo.currentText().strip()
        if not troncon_layer_id or not troncon_field:
            QMessageBox.warning(
                self,
                "Configuration incomplète",
                "Veuillez sélectionner une couche tronçon et son champ identifiant.",
            )
            return
        save_config(
            {
                "troncon_layer_id": troncon_layer_id,
                "troncon_field": troncon_field,
                "branchement_layer_id": branch_layer_id,
                "branchement_field": branch_field,
            }
        )
        self.accept()
