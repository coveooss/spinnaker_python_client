# coding: utf-8

"""
    Spinnaker API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from spinnaker-python-client.api_client import ApiClient


class CiControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_build_output_by_id_using_get(self, build_id, **kwargs):  # noqa: E501
        """getBuildOutputById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_output_by_id_using_get(build_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_id: buildId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_build_output_by_id_using_get_with_http_info(build_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_build_output_by_id_using_get_with_http_info(build_id, **kwargs)  # noqa: E501
            return data

    def get_build_output_by_id_using_get_with_http_info(self, build_id, **kwargs):  # noqa: E501
        """getBuildOutputById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_output_by_id_using_get_with_http_info(build_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_id: buildId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_build_output_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_id' is set
        if ('build_id' not in params or
                params['build_id'] is None):
            raise ValueError("Missing the required parameter `build_id` when calling `get_build_output_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'build_id' in params:
            path_params['buildId'] = params['build_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ci/builds/{buildId}/output', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_builds_using_get1(self, **kwargs):  # noqa: E501
        """getBuilds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_builds_using_get1(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_number: buildNumber
        :param str commit_id: commitId
        :param str completion_status: completionStatus
        :param str project_key: projectKey
        :param str repo_slug: repoSlug
        :return: list[Mapstringobject]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_builds_using_get1_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_builds_using_get1_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_builds_using_get1_with_http_info(self, **kwargs):  # noqa: E501
        """getBuilds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_builds_using_get1_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_number: buildNumber
        :param str commit_id: commitId
        :param str completion_status: completionStatus
        :param str project_key: projectKey
        :param str repo_slug: repoSlug
        :return: list[Mapstringobject]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_number', 'commit_id', 'completion_status', 'project_key', 'repo_slug']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_builds_using_get1" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'build_number' in params:
            query_params.append(('buildNumber', params['build_number']))  # noqa: E501
        if 'commit_id' in params:
            query_params.append(('commitId', params['commit_id']))  # noqa: E501
        if 'completion_status' in params:
            query_params.append(('completionStatus', params['completion_status']))  # noqa: E501
        if 'project_key' in params:
            query_params.append(('projectKey', params['project_key']))  # noqa: E501
        if 'repo_slug' in params:
            query_params.append(('repoSlug', params['repo_slug']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ci/builds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Mapstringobject]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
