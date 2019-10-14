# import re
# from collections import namedtuple
# from inspect import getdoc, isclass

from robot.api import logger
# from robot.errors import DataError
# from robot.libraries.BuiltIn import BuiltIn
# from robot.utils.importer import Importer

from TestLib.base import DynamicCore
from .keywords.comparisionkeywords import ComparisionKeywords
from .keywords.reportkeywords import ReportKeywords

__version__ = '1.0.0'


class TestLib(DynamicCore):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        libraries = [
            ComparisionKeywords(),
            ReportKeywords()
        ]
        DynamicCore.__init__(self, libraries)

    def run_keyword(self, name, args, kwargs):
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            logger.warn("Failed to run kws")

    def get_keyword_tags(self, name):
        tags = list(DynamicCore.get_keyword_tags(self, name))
        return tags

    def get_keyword_documentation(self, name):
        if name == '__intro__':
            return self._get_intro_documentation()
        return DynamicCore.get_keyword_documentation(self, name)