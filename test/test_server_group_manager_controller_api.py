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
from spinnaker-python-client.api.server_group_manager_controller_api import ServerGroupManagerControllerApi  # noqa: E501
from spinnaker-python-client.rest import ApiException


class TestServerGroupManagerControllerApi(unittest.TestCase):
    """ServerGroupManagerControllerApi unit test stubs"""

    def setUp(self):
        self.api = spinnaker-python-client.api.server_group_manager_controller_api.ServerGroupManagerControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_server_group_managers_for_application_using_get(self):
        """Test case for get_server_group_managers_for_application_using_get

        Retrieve a list of server group managers for an application  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
