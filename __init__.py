# -----------------------------------------------------------
# Copyright (C) 2015 Martin Dobias
# -----------------------------------------------------------

import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from .dialog import XmlReaderDialog

# ruff: noqa
from .resources import *


def classFactory(iface):
    return MinimalPlugin(iface)


class MinimalPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.dialog = None

    def initGui(self):
        icon_path = ":/plugins/QITV/icon.svg"
        print("Icon path:", icon_path)
        print("Exists?", os.path.exists(icon_path))
        self.action = QAction(QIcon(icon_path), "Go!", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        if not self.dialog:
            self.dialog = XmlReaderDialog(self.iface.mainWindow())
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()
