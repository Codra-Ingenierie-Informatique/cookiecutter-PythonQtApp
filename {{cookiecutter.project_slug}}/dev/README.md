Development platform
====================

Python distribution
-------------------

Reference platform is based on:

* WinPython WPy64-31001 (Python 3.10.0)

* With packages listed in "pip_list.txt"

Environment variables
---------------------

How to use Visual Studio Code launch configurations and tasks (`launch.json`
and `tasks.json`):

    ```bat
    @REM Development environment
    set {{cookiecutter.python_executable_env_var}}=C:\Apps\WPy64-31001-{{ cookiecutter.project_name }}\python-3.10.0.amd64\python.exe
    ```
