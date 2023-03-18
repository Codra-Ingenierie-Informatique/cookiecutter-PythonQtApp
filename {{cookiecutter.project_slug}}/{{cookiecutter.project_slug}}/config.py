# -*- coding: utf-8 -*-

"""
{{cookiecutter.project_slug}}.config

The `config` module handles `{{cookiecutter.project_slug}}` configuration.
"""

import os
import os.path as osp

from guidata import configtools

from {{cookiecutter.project_slug}}.utils import conf

_ = configtools.get_translation("{{cookiecutter.project_slug}}")

configtools.add_image_module_path("{{cookiecutter.project_slug}}", "data")

CONF_VERSION = "1.0.0"
APP_NAME = _("{{ cookiecutter.project_name }}")
APP_DESC = _("""{{ cookiecutter.project_short_description }}""")

DEBUG_VAR_STR = "{{cookiecutter.project_slug.upper()}}DEBUG"
try:
    DEBUG = int(os.environ.get(DEBUG_VAR_STR, ""))
except ValueError:
    DEBUG = 1 if len(os.environ.get(DEBUG_VAR_STR, "")) > 0 else 0

DATETIME_FORMAT = "%d/%m/%Y - %H:%M:%S"


DATAPATH = configtools.get_module_data_path("{{cookiecutter.project_slug}}", relpath="data")
TESTPATH = configtools.get_module_data_path("{{cookiecutter.project_slug}}", relpath="tests")


class MainSection(conf.Section, metaclass=conf.SectionMeta):
    """Class defining the main configuration section structure.
    Each class attribute is an option (metaclass is automatically affecting
    option names in .INI file based on class attribute names)."""

    traceback_log_path = conf.ConfigPathOption()
    traceback_log_available = conf.Option()
    faulthandler_enabled = conf.Option()
    faulthandler_log_path = conf.ConfigPathOption()
    faulthandler_log_available = conf.Option()
    window_maximized = conf.Option()
    window_position = conf.Option()
    window_size = conf.Option()
    base_dir = conf.WorkingDirOption()
    recent_files = conf.RecentFilesOption()


# Usage (example): Conf.console.enable.get(True)
class Conf(conf.Configuration, metaclass=conf.ConfMeta):
    """Class defining CodraFT configuration structure.
    Each class attribute is a section (metaclass is automatically affecting
    section names in .INI file based on class attribute names)."""

    main = MainSection()


def get_old_log_fname(fname):
    """Return old log fname from current log fname"""
    return osp.splitext(fname)[0] + ".1.log"


def initialize():
    """Initialize application configuration"""
    Conf.initialize(APP_NAME, CONF_VERSION, load=not DEBUG)
    Conf.main.traceback_log_path.set(f".{APP_NAME}_traceback.log")
    Conf.main.faulthandler_log_path.set(f".{APP_NAME}_faulthandler.log")


def reset():
    """Reset application configuration"""
    Conf.reset()
    initialize()


initialize()
