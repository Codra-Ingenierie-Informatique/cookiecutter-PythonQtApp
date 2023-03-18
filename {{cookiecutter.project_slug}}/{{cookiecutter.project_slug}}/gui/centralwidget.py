# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_name }} central widget"""

# pylint: disable=no-name-in-module
# pylint: disable=no-member

import qtpy.QtCore as QC
import qtpy.QtWidgets as QW


class CentralWidget(QW.QWidget):
    """{{ cookiecutter.project_name }} central widget"""

    SIG_MODIFIED = QC.Signal()
    SIG_MESSAGE = QC.Signal(str, int)

    def __init__(self):
        super().__init__()
        self.setMinimumSize(850, 400)
        self.setAttribute(QC.Qt.WA_DeleteOnClose)
        self.path = None

        widget = QW.QLabel("Empty widget")
        vlayout = QW.QVBoxLayout()
        vlayout.addWidget(widget)
        self.setLayout(vlayout)

    def get_menu_actions(self):
        """Return menu actions"""
        return {}

    def get_toolbars(self):
        """Return toolbars"""
        return []

    def new_file(self):
        """New file"""

    def load_file(self, path):
        """Load file"""
        self.path = path

    def save_file(self, path):
        """Save file"""
        self.path = path
