from SudsLibrary import SudsLibrary
from .extendedclientmanagement import _ExtendedClientManagementKeywords
from .extendedproxy import _ExtendedProxyKeywords
from .version import VERSION
from robot.libraries import OperatingSystem


__version__ = VERSION


class ExtendedSudsLibrary(SudsLibrary, _ExtendedClientManagementKeywords, _ExtendedProxyKeywords):
    """
    ExtendedSudsLibrary is a library for functional testing of SOAP-based web services. It is extended from [https://github.com/ludovicurbain/robotframework-sudslibrary|SudsLibrary].
    """

    ROBOT_LIBRARY_VERSION = __version__
