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
from spinnaker-python-client.api.plugin_publish_controller_api import PluginPublishControllerApi  # noqa: E501
from spinnaker-python-client.rest import ApiException


class TestPluginPublishControllerApi(unittest.TestCase):
    """PluginPublishControllerApi unit test stubs"""

    def setUp(self):
        self.api = spinnaker-python-client.api.plugin_publish_controller_api.PluginPublishControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_publish_plugin_using_post(self):
        """Test case for publish_plugin_using_post

        Publish a plugin binary and the plugin info metadata.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()