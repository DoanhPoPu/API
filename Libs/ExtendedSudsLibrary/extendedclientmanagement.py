from SudsLibrary.clientmanagement import _ClientManagementKeywords
import os
import urllib
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
from suds.client import Client
from suds.xsd.doctor import ImportDoctor
from SudsLibrary.utils import *

class _ExtendedClientManagementKeywords(_ClientManagementKeywords):
    """
    This class is customized from ClientManagementKeywords to make compatible with python 3 and current project.
    """
    def _get_url(self, url_or_path):
        if not len(urlparse(url_or_path).scheme) > 1:
            if not os.path.isfile(url_or_path):
                raise IOError("File '%s' not found." % url_or_path)
            url_or_path = 'file:' + urllib.request.pathname2url(url_or_path)
        return url_or_path

    def create_soap_client(self, url_or_path, alias=None, autoblend=False, timeout='90 seconds', unwrap=False):
        """Loads a WSDL from the given URL/path and creates a Suds SOAP client.

        Returns the index of this client instance which can be used later to
        switch back to it. See `Switch Soap Client` for example.

        Optional alias is an alias for the client instance and it can be used
        for switching between clients (just as index can be used). See `Switch
        Soap Client` for more details.

        Autoblend ensures that the schema(s) defined within the WSDL import
        each other.

        `timeout` sets the timeout for SOAP requests and must be given in
        Robot Framework's time format (e.g. '1 minute', '2 min 3 s', '4.5').

        `unwrap` is set to False by default.

        Examples:
        | Create Soap Client | http://localhost:8080/ws/Billing.asmx?WSDL |
        | Create Soap Client | ${CURDIR}/../wsdls/tracking.wsdl |
        | Create Soap Client | http://localhost:8080/ws/Billing.asmx?WSDL | unwrap=True |
        """
        url = self._get_url(url_or_path)
        autoblend = to_bool(autoblend)
        kwargs = {'autoblend': autoblend}
        imports = self._imports
        if imports:
            self._log_imports()
            kwargs['doctor'] = ImportDoctor(*imports)
        client = Client(url, **kwargs, unwrap=unwrap)
        index = self._add_client(client, alias)
        self._set_soap_timeout(timeout)
        return index

    def conver_to_dict(cls, suds_object):
        """
        Convert a sudsobject into a dictionary.
        :param suds_object - A suds object
        :return: dict - A python dictionary containing the items contained in sobject.
        """
        required_dict = Client.dict(suds_object)
        return required_dict
