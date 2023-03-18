# -*- coding: utf-8 -*-
"""Testing {{ cookiecutter.project_name }} central widget"""

import os.path as osp

from guidata import qapplication

from {{cookiecutter.project_slug}}.config import TESTPATH
from {{cookiecutter.project_slug}}.gui.centralwidget import CentralWidget


def test():
    """Test central widget"""
    app = qapplication()
    widget = CentralWidget()
    widget.setWindowTitle("{{ cookiecutter.project_name }} central widget")
    widget.show()
    widget.load_file(osp.join(TESTPATH, "test{{cookiecutter.file_extension}}"))
    app.exec_()


if __name__ == "__main__":
    test()
