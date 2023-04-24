#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PYTHON_EXECUTABLE = os.environ["{{cookiecutter.python_executable_env_var}}"]


def remove_file(filepath):
    """Remove a file from the project directory."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def is_winpython_install():
    """Return True if the Python executable is in a WinPython directory."""
    scripts = os.path.join(os.path.dirname(PYTHON_EXECUTABLE), os.pardir, "scripts")
    return os.path.isfile(os.path.join(scripts, "env_for_icons.bat"))


def create_bat_launcher():
    """Create a .bat launcher for Windows.

    Only works for a WinPython distribution without a virtual environment."""
    bat_file = os.path.join(PROJECT_DIRECTORY, "{{cookiecutter.project_slug}}.bat")
    with open(bat_file, "w") as bat:
        bat.write(
            f"""@echo off
cd/D "%{{cookiecutter.python_executable_env_var}}%\scripts\"
call "env_for_icons.bat" %*
cd/D %~dp0
set PYTHONPATH=%cd%
start "" "%WINPYDIR%\pythonw.exe" -m {{cookiecutter.project_slug}}.app %*"""
        )


if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
    if not is_winpython_install():
        remove_file("{{cookiecutter.project_slug}}.bat")
