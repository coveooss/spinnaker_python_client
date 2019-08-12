# coding: utf-8

"""
    Spinnaker API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.webhook_controller_api import WebhookControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWebhookControllerApi(unittest.TestCase):
    """WebhookControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.webhook_controller_api.WebhookControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_preconfigured_webhooks_using_get(self):
        """Test case for preconfigured_webhooks_using_get

        Retrieve a list of preconfigured webhooks in Orca  # noqa: E501
        """
        pass

    def test_webhooks_using_post(self):
        """Test case for webhooks_using_post

        Endpoint for posting webhooks to Spinnaker's webhook service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()