import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from .dialog import XmlReaderDialog, ExportDialog
from .settings_dialog import SettingsDialog

# ruff: noqa
from .resources import *


def classFactory(iface):
    return QITV(iface)


class QITV:
    def __init__(self, iface):
        self.iface = iface
        self.import_dialog = None
        self.export_dialog = None

    def initGui(self):
        self.import_action = QAction(
            QIcon(":/plugins/QITV/import.svg"),
            "Importer ITV",
            self.iface.mainWindow(),
        )
        self.import_action.triggered.connect(self.run_import)
        self.iface.addToolBarIcon(self.import_action)

        self.export_action = QAction(
            QIcon(":/plugins/QITV/export.svg"),
            "Exporter ITV",
            self.iface.mainWindow(),
        )
        self.export_action.triggered.connect(self.run_export)
        self.iface.addToolBarIcon(self.export_action)

        self.settings_action = QAction(
            "Paramètres QITV",
            self.iface.mainWindow(),
        )
        self.settings_action.triggered.connect(self.run_settings)

        self.iface.addPluginToMenu("QITV", self.import_action)
        self.iface.addPluginToMenu("QITV", self.export_action)
        self.iface.addPluginToMenu("QITV", self.settings_action)

    def unload(self):
        self.iface.removeToolBarIcon(self.import_action)
        self.iface.removeToolBarIcon(self.export_action)
        self.iface.removePluginMenu("QITV", self.import_action)
        self.iface.removePluginMenu("QITV", self.export_action)
        self.iface.removePluginMenu("QITV", self.settings_action)
        del self.import_action
        del self.export_action
        del self.settings_action

    def run_import(self):
        if not self.import_dialog:
            self.import_dialog = XmlReaderDialog(self.iface.mainWindow())
        self.import_dialog.show()
        self.import_dialog.raise_()
        self.import_dialog.activateWindow()

    def run_export(self):
        if not self.export_dialog:
            self.export_dialog = ExportDialog(self.iface.mainWindow())
        self.export_dialog.show()
        self.export_dialog.raise_()
        self.export_dialog.activateWindow()

    def run_settings(self):
        dlg = SettingsDialog(self.iface.mainWindow())
        dlg.exec_()
        self.import_dialog = None
        self.export_dialog = None
