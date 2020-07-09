# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import bloxonednsconfig
from bloxonednsconfig.api.server_api import ServerApi  # noqa: E501
from bloxonednsconfig.rest import ApiException


class TestServerApi(unittest.TestCase):
    """ServerApi unit test stubs"""

    def setUp(self):
        self.api = bloxonednsconfig.api.server_api.ServerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_server_create(self):
        """Test case for server_create

        Create the Server object.  # noqa: E501
        """
        pass

    def test_server_delete(self):
        """Test case for server_delete

        Delete the Server object.  # noqa: E501
        """
        pass

    def test_server_list(self):
        """Test case for server_list

        List Server objects.  # noqa: E501
        """
        pass

    def test_server_read(self):
        """Test case for server_read

        Read the Server object.  # noqa: E501
        """
        pass

    def test_server_update(self):
        """Test case for server_update

        Update the Server object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
