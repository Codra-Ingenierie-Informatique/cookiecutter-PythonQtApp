# -*- coding: utf-8 -*-

"""
Application runner for {{ cookiecutter.project_name }}.
"""

# pylint: disable=no-name-in-module

import sys

from guidata.configtools import get_image_file_path
from qtpy.QtCore import Qt
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QSplashScreen

#  Local imports
from {{cookiecutter.project_slug}}.gui.mainwindow import MainWindow
from {{cookiecutter.project_slug}}.utils.qthelpers import qt_app_context


def run(fname=None):
    """Run {{ cookiecutter.project_name }}"""
    if fname is None and len(sys.argv) > 1:
        fname = sys.argv[1]
    with qt_app_context(exec_loop=True):
        # Showing splash screen
        ssfname = get_image_file_path("{{cookiecutter.project_slug}}.png", "")
        if ssfname:
            pixmap = QPixmap(ssfname)
            splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
            splash.show()
        window = MainWindow(fname)
        window.show()
        if ssfname:
            splash.finish(window)
        window.check_for_previous_crash()


if __name__ == "__main__":
    run()
