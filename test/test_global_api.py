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
from bloxonednsconfig.api.global_api import GlobalApi  # noqa: E501
from bloxonednsconfig.rest import ApiException


class TestGlobalApi(unittest.TestCase):
    """GlobalApi unit test stubs"""

    def setUp(self):
        self.api = bloxonednsconfig.api.global_api.GlobalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_global_read(self):
        """Test case for global_read

        Read the Global configuration object.  # noqa: E501
        """
        pass

    def test_global_read2(self):
        """Test case for global_read2

        Read the Global configuration object.  # noqa: E501
        """
        pass

    def test_global_update(self):
        """Test case for global_update

        Update the Global configuration object.  # noqa: E501
        """
        pass

    def test_global_update2(self):
        """Test case for global_update2

        Update the Global configuration object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
