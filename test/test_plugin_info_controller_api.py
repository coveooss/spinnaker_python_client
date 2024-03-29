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
from spinnaker-python-client.api.plugin_info_controller_api import PluginInfoControllerApi  # noqa: E501
from spinnaker-python-client.rest import ApiException


class TestPluginInfoControllerApi(unittest.TestCase):
    """PluginInfoControllerApi unit test stubs"""

    def setUp(self):
        self.api = spinnaker-python-client.api.plugin_info_controller_api.PluginInfoControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_plugin_info_using_delete(self):
        """Test case for delete_plugin_info_using_delete

        Delete plugin info with the provided Id  # noqa: E501
        """
        pass

    def test_get_all_plugin_info_using_get(self):
        """Test case for get_all_plugin_info_using_get

        Get all plugin info objects  # noqa: E501
        """
        pass

    def test_persist_plugin_info_using_post(self):
        """Test case for persist_plugin_info_using_post

        Persist plugin metadata information  # noqa: E501
        """
        pass

    def test_persist_plugin_info_using_put(self):
        """Test case for persist_plugin_info_using_put

        Persist plugin metadata information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
