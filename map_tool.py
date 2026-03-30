"""
map_tool.py
A minimal QgsMapTool that emits one feature-picked signal then deactivates.
Used by TubeDialog to fill the AAA field from a map click.
"""

from qgis.core import QgsGeometry
from qgis.gui import QgsMapTool
from qgis.PyQt.QtCore import Qt, pyqtSignal
from qgis.PyQt.QtGui import QCursor


class FeaturePickerTool(QgsMapTool):
    """
    Single-use map tool.

    After the user clicks on the canvas the tool:
      1. Finds the closest feature in `layer` within a small tolerance.
      2. Emits `feature_picked(value)` with the string value of `field_name`.
      3. Restores the previous map tool automatically.
    """

    feature_picked = pyqtSignal(str)

    def __init__(self, canvas, layer, field_name):
        super().__init__(canvas)
        self._layer = layer
        self._field_name = field_name
        self._previous_tool = canvas.mapTool()
        self.setCursor(QCursor(Qt.CrossCursor))

    def canvasReleaseEvent(self, event):  # noqa: N802
        """Triggered on mouse release — find the nearest feature and emit."""
        point = self.toLayerCoordinates(self._layer, event.pos())
        radius = self.canvas().extent().width() * 5 / self.canvas().width()
        request_rect = QgsGeometry.fromPointXY(point).buffer(radius, 5).boundingBox()
        value = ""
        best_dist = float("inf")
        for feat in self._layer.getFeatures(request_rect):
            geom = feat.geometry()
            if geom is None:
                continue
            dist = geom.distance(
                __import__(
                    "qgis.core", fromlist=["QgsGeometry"]
                ).QgsGeometry.fromPointXY(point)
            )
            if dist < best_dist:
                best_dist = dist
                val = feat.attribute(self._field_name)
                value = str(val) if val is not None else ""
        self.feature_picked.emit(value)
        self.canvas().setMapTool(self._previous_tool)

    def keyPressEvent(self, event):
        """Allow Escape to cancel without emitting."""
        if event.key() == Qt.Key_Escape:
            self.canvas().setMapTool(self._previous_tool)
