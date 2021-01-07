# coding: utf-8

"""
    Spinnaker API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import spinnaker-python-client
from spinnaker-python-client.api.network_controller_api import NetworkControllerApi  # noqa: E501
from spinnaker-python-client.rest import ApiException


class TestNetworkControllerApi(unittest.TestCase):
    """NetworkControllerApi unit test stubs"""

    def setUp(self):
        self.api = spinnaker-python-client.api.network_controller_api.NetworkControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_by_cloud_provider_using_get(self):
        """Test case for all_by_cloud_provider_using_get

        Retrieve a list of networks for a given cloud provider  # noqa: E501
        """
        pass

    def test_all_using_get2(self):
        """Test case for all_using_get2

        Retrieve a list of networks, grouped by cloud provider  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
