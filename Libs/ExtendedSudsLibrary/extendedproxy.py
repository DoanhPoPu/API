from SudsLibrary.proxy import RawSoapMessage
from SudsLibrary.proxy import _ProxyKeywords


class ExtendedRawSoapMessage(RawSoapMessage):

    def __init__(self, string):
        if isinstance(string, str):
            self.message = string.encode('UTF-8')
        else:
            self.message = str(string)


class _ExtendedProxyKeywords(_ProxyKeywords):
    """
    This class is customized from ClientManagementKeywords to make compatible with python 3 and current project.
    """
    def create_raw_soap_message(self, message):
        return ExtendedRawSoapMessage(message)
