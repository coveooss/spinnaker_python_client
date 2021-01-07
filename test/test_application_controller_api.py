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
from spinnaker-python-client.api.application_controller_api import ApplicationControllerApi  # noqa: E501
from spinnaker-python-client.rest import ApiException


class TestApplicationControllerApi(unittest.TestCase):
    """ApplicationControllerApi unit test stubs"""

    def setUp(self):
        self.api = spinnaker-python-client.api.application_controller_api.ApplicationControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_pipeline_using_put(self):
        """Test case for cancel_pipeline_using_put

        Cancel pipeline  # noqa: E501
        """
        pass

    def test_cancel_task_using_put(self):
        """Test case for cancel_task_using_put

        Cancel task  # noqa: E501
        """
        pass

    def test_get_all_applications_using_get(self):
        """Test case for get_all_applications_using_get

        Retrieve a list of applications  # noqa: E501
        """
        pass

    def test_get_application_history_using_get(self):
        """Test case for get_application_history_using_get

        Retrieve a list of an application's configuration revision history  # noqa: E501
        """
        pass

    def test_get_application_using_get(self):
        """Test case for get_application_using_get

        Retrieve an application's details  # noqa: E501
        """
        pass

    def test_get_pipeline_config_using_get(self):
        """Test case for get_pipeline_config_using_get

        Retrieve a pipeline configuration  # noqa: E501
        """
        pass

    def test_get_pipeline_configs_for_application_using_get(self):
        """Test case for get_pipeline_configs_for_application_using_get

        Retrieve a list of an application's pipeline configurations  # noqa: E501
        """
        pass

    def test_get_pipelines_using_get(self):
        """Test case for get_pipelines_using_get

        Retrieve a list of an application's pipeline executions  # noqa: E501
        """
        pass

    def test_get_strategy_config_using_get(self):
        """Test case for get_strategy_config_using_get

        Retrieve a pipeline strategy configuration  # noqa: E501
        """
        pass

    def test_get_strategy_configs_for_application_using_get(self):
        """Test case for get_strategy_configs_for_application_using_get

        Retrieve a list of an application's pipeline strategy configurations  # noqa: E501
        """
        pass

    def test_get_task_details_using_get(self):
        """Test case for get_task_details_using_get

        Get task details  # noqa: E501
        """
        pass

    def test_get_task_using_get(self):
        """Test case for get_task_using_get

        Get task  # noqa: E501
        """
        pass

    def test_get_tasks_using_get(self):
        """Test case for get_tasks_using_get

        Retrieve a list of an application's tasks  # noqa: E501
        """
        pass

    def test_invoke_pipeline_config_using_post(self):
        """Test case for invoke_pipeline_config_using_post

        Invoke pipeline config  # noqa: E501
        """
        pass

    def test_task_using_post(self):
        """Test case for task_using_post

        Create task  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
