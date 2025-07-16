from qgis.core import (
    QgsApplication,
    QgsMapLayer,
    QgsProject,
    QgsWkbTypes,
)
from qgis.PyQt.QtWidgets import (
    QComboBox,
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from .decoder import itv_parser
from .processing import ProcessingTask


class XmlReaderDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Import XML NF EN 13508-2")
        self.resize(400, 600)
        QgsProject.instance().layerWasAdded.connect(self.populate_line_layers)
        QgsProject.instance().layersRemoved.connect(self.populate_line_layers)
        QgsProject.instance().layerWillBeRemoved.connect(self.populate_line_layers)
        main_layout = QVBoxLayout()

        # File browse layout
        file_layout = QHBoxLayout()
        self.label = QLabel("Selectionner un fichier XML:")
        self.line_edit = QLineEdit()
        self.line_edit.setReadOnly(True)
        self.btn_browse = QPushButton("Parcourir")
        file_layout.addWidget(self.label)
        file_layout.addWidget(self.line_edit)
        file_layout.addWidget(self.btn_browse)

        # Layer + field selection layout
        layer_layout = QHBoxLayout()
        self.layer_label = QLabel("Couche tronçon:")
        self.layer_combo = QComboBox()
        self.field_label = QLabel("Identifiant:")
        self.field_combo = QComboBox()

        layer_layout.addWidget(self.layer_label)
        layer_layout.addWidget(self.layer_combo)
        layer_layout.addWidget(self.field_label)
        layer_layout.addWidget(self.field_combo)

        # Process button
        self.btn_process = QPushButton("Traiter")

        # Text display widget
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        main_layout.addLayout(file_layout)
        main_layout.addLayout(layer_layout)
        main_layout.addWidget(self.btn_process)
        main_layout.addWidget(self.text_edit)

        self.setLayout(main_layout)

        # Connections
        self.btn_browse.clicked.connect(self.browse_file)
        self.btn_process.clicked.connect(self.process_all)
        self.layer_combo.currentIndexChanged.connect(self.populate_fields_for_layer)

        self.populate_line_layers()

        # Keep track of task so we can disable button etc
        self.current_task = None

    def populate_line_layers(self):
        self.layer_combo.clear()
        project = QgsProject.instance()
        layers = project.mapLayers().values()
        line_layers = [
            layer
            for layer in layers
            if layer.type() == QgsMapLayer.VectorLayer
            and QgsWkbTypes.geometryType(layer.wkbType()) == QgsWkbTypes.LineGeometry
        ]
        for layer in line_layers:
            self.layer_combo.addItem(layer.name(), layer.id())

        self.populate_fields_for_layer()

    def populate_fields_for_layer(self):
        self.field_combo.clear()
        layer_id = self.layer_combo.currentData()
        if not layer_id:
            return
        project = QgsProject.instance()
        layer = project.mapLayer(layer_id)
        if not layer:
            return

        fields = layer.fields()
        for field in fields:
            self.field_combo.addItem(field.name())

    def browse_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Ouvrir un fichier XML ou TXT",
            "",
            "Fichiers XML ou TXT (*.xml *.txt);;Tous les fichiers (*)",
        )
        if filename:
            self.line_edit.setText(filename)

    def process_all(self):
        if self.current_task is not None:
            # A task is already running; ignore multiple clicks
            return

        filename = self.line_edit.text()
        if not filename:
            self.text_edit.setPlainText("Aucun fichier Xml selectionné.")
            return

        try:
            content = itv_parser(filename)
        except Exception as e:
            self.text_edit.setPlainText(f"Erreur de lectue du fichier XML:\n{e}.")
            return

        layer_id = self.layer_combo.currentData()
        selected_field = self.field_combo.currentText()

        if not layer_id:
            self.text_edit.setPlainText("Aucune couche de tronçons n’est sélectionnée.")
            return

        if not selected_field:
            self.text_edit.setPlainText("Aucun identifiant sélectionné.")
            return

        # Disable button while processing
        self.btn_process.setEnabled(False)
        self.text_edit.setPlainText("Traitement... Veuillez patienter.")

        # Create and start the task
        task_desc = "Traitement du fichier XML"
        self.current_task = ProcessingTask(
            task_desc, filename, content, layer_id, selected_field
        )
        self.current_task.taskCompleted.connect(self.task_finished)

        QgsApplication.taskManager().addTask(self.current_task)

    def task_finished(self):
        self.btn_process.setEnabled(True)

        if self.current_task.error:
            self.text_edit.setPlainText(
                f"Erreur lros du traitement:\n{self.current_task.error}"
            )
        else:
            self.text_edit.setPlainText(self.current_task.result_text)

        self.current_task = None
