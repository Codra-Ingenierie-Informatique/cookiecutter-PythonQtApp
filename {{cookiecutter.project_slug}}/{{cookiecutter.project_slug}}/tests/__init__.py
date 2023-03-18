# -*- coding: utf-8 -*-

"""
{{ cookiecutter.project_name }} unit tests
"""

from guidata.guitest import run_testlauncher

import {{cookiecutter.project_slug}}.config  # Loading icons


def run():
    """Run {{ cookiecutter.project_name }} test launcher"""
    run_testlauncher({{cookiecutter.project_slug}})


if __name__ == "__main__":
    run()
