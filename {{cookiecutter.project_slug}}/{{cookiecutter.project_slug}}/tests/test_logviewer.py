# -*- coding: utf-8 -*-

"""
{{ cookiecutter.project_name }} Log viewer test
"""

from {{cookiecutter.project_slug}}.gui.logviewer import exec_logviewer_dialog
from {{cookiecutter.project_slug}}.utils.qthelpers import qt_app_context

SHOW = True  # Show test in GUI-based test launcher


def test_log_viewer():
    """Test {{ cookiecutter.project_name }} log viewer window"""
    with qt_app_context():
        exec_logviewer_dialog()


if __name__ == "__main__":
    test_log_viewer()
