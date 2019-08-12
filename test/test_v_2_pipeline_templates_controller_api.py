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
from swagger_client.api.v_2_pipeline_templates_controller_api import V2PipelineTemplatesControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestV2PipelineTemplatesControllerApi(unittest.TestCase):
    """V2PipelineTemplatesControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.v_2_pipeline_templates_controller_api.V2PipelineTemplatesControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_using_post1(self):
        """Test case for create_using_post1

        (ALPHA) Create a pipeline template.  # noqa: E501
        """
        pass

    def test_delete_using_delete1(self):
        """Test case for delete_using_delete1

        Delete a pipeline template.  # noqa: E501
        """
        pass

    def test_get_using_get2(self):
        """Test case for get_using_get2

        (ALPHA) Get a pipeline template.  # noqa: E501
        """
        pass

    def test_list_pipeline_template_dependents_using_get1(self):
        """Test case for list_pipeline_template_dependents_using_get1

        (ALPHA) List all pipelines that implement a pipeline template  # noqa: E501
        """
        pass

    def test_list_using_get1(self):
        """Test case for list_using_get1

        (ALPHA) List pipeline templates.  # noqa: E501
        """
        pass

    def test_plan_using_post(self):
        """Test case for plan_using_post

        (ALPHA) Plan a pipeline template configuration.  # noqa: E501
        """
        pass

    def test_update_using_post1(self):
        """Test case for update_using_post1

        (ALPHA) Update a pipeline template.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()