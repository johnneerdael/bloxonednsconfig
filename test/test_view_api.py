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
from bloxonednsconfig.api.view_api import ViewApi  # noqa: E501
from bloxonednsconfig.rest import ApiException


class TestViewApi(unittest.TestCase):
    """ViewApi unit test stubs"""

    def setUp(self):
        self.api = bloxonednsconfig.api.view_api.ViewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_view_create(self):
        """Test case for view_create

        Create the View object.  # noqa: E501
        """
        pass

    def test_view_delete(self):
        """Test case for view_delete

        Delete the View object.  # noqa: E501
        """
        pass

    def test_view_list(self):
        """Test case for view_list

        List View objects.  # noqa: E501
        """
        pass

    def test_view_read(self):
        """Test case for view_read

        Read the View object.  # noqa: E501
        """
        pass

    def test_view_update(self):
        """Test case for view_update

        Update the View object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()