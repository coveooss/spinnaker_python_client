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
from spinnaker-python-client.api.v_2_canary_config_controller_api import V2CanaryConfigControllerApi  # noqa: E501
from spinnaker-python-client.rest import ApiException


class TestV2CanaryConfigControllerApi(unittest.TestCase):
    """V2CanaryConfigControllerApi unit test stubs"""

    def setUp(self):
        self.api = spinnaker-python-client.api.v_2_canary_config_controller_api.V2CanaryConfigControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_canary_config_using_post(self):
        """Test case for create_canary_config_using_post

        Create a canary configuration  # noqa: E501
        """
        pass

    def test_delete_canary_config_using_delete(self):
        """Test case for delete_canary_config_using_delete

        Delete a canary configuration  # noqa: E501
        """
        pass

    def test_get_canary_config_using_get(self):
        """Test case for get_canary_config_using_get

        Retrieve a canary configuration by id  # noqa: E501
        """
        pass

    def test_get_canary_configs_using_get(self):
        """Test case for get_canary_configs_using_get

        Retrieve a list of canary configurations  # noqa: E501
        """
        pass

    def test_update_canary_config_using_put(self):
        """Test case for update_canary_config_using_put

        Update a canary configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()