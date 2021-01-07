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

from spinnaker_client.api_client import ApiClient


class BuildControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_build_masters_using_get(self, **kwargs):  # noqa: E501
        """Get build masters  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_masters_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: type
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_build_masters_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_build_masters_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_build_masters_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get build masters  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_masters_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: type
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_build_masters_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

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
            '/v2/builds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_build_using_get(self, build_master, number, **kwargs):  # noqa: E501
        """Get build for build master  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_using_get(build_master, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :param str number: number (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_build_using_get_with_http_info(build_master, number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_build_using_get_with_http_info(build_master, number, **kwargs)  # noqa: E501
            return data

    def get_build_using_get_with_http_info(self, build_master, number, **kwargs):  # noqa: E501
        """Get build for build master  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_using_get_with_http_info(build_master, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :param str number: number (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_master', 'number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_build_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_master' is set
        if ('build_master' not in params or
                params['build_master'] is None):
            raise ValueError("Missing the required parameter `build_master` when calling `get_build_using_get`")  # noqa: E501
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `get_build_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'build_master' in params:
            path_params['buildMaster'] = params['build_master']  # noqa: E501
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

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
            '/v2/builds/{buildMaster}/build/{number}/**', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_builds_using_get(self, build_master, **kwargs):  # noqa: E501
        """Get builds for build master  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_builds_using_get(build_master, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_builds_using_get_with_http_info(build_master, **kwargs)  # noqa: E501
        else:
            (data) = self.get_builds_using_get_with_http_info(build_master, **kwargs)  # noqa: E501
            return data

    def get_builds_using_get_with_http_info(self, build_master, **kwargs):  # noqa: E501
        """Get builds for build master  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_builds_using_get_with_http_info(build_master, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_master']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_builds_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_master' is set
        if ('build_master' not in params or
                params['build_master'] is None):
            raise ValueError("Missing the required parameter `build_master` when calling `get_builds_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'build_master' in params:
            path_params['buildMaster'] = params['build_master']  # noqa: E501

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
            '/v2/builds/{buildMaster}/builds/**', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_job_config_using_get(self, build_master, **kwargs):  # noqa: E501
        """Get job config  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_config_using_get(build_master, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_job_config_using_get_with_http_info(build_master, **kwargs)  # noqa: E501
        else:
            (data) = self.get_job_config_using_get_with_http_info(build_master, **kwargs)  # noqa: E501
            return data

    def get_job_config_using_get_with_http_info(self, build_master, **kwargs):  # noqa: E501
        """Get job config  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_config_using_get_with_http_info(build_master, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_master']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_job_config_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_master' is set
        if ('build_master' not in params or
                params['build_master'] is None):
            raise ValueError("Missing the required parameter `build_master` when calling `get_job_config_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'build_master' in params:
            path_params['buildMaster'] = params['build_master']  # noqa: E501

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
            '/v2/builds/{buildMaster}/jobs/**', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_jobs_for_build_master_using_get(self, build_master, **kwargs):  # noqa: E501
        """Get jobs for build master  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_jobs_for_build_master_using_get(build_master, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_jobs_for_build_master_using_get_with_http_info(build_master, **kwargs)  # noqa: E501
        else:
            (data) = self.get_jobs_for_build_master_using_get_with_http_info(build_master, **kwargs)  # noqa: E501
            return data

    def get_jobs_for_build_master_using_get_with_http_info(self, build_master, **kwargs):  # noqa: E501
        """Get jobs for build master  # noqa: E501

        Deprecated, use the v3 endpoint instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_jobs_for_build_master_using_get_with_http_info(build_master, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_master']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_jobs_for_build_master_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_master' is set
        if ('build_master' not in params or
                params['build_master'] is None):
            raise ValueError("Missing the required parameter `build_master` when calling `get_jobs_for_build_master_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'build_master' in params:
            path_params['buildMaster'] = params['build_master']  # noqa: E501

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
            '/v2/builds/{buildMaster}/jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v3_get_build_masters_using_get(self, **kwargs):  # noqa: E501
        """Get build masters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_build_masters_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: type
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v3_get_build_masters_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v3_get_build_masters_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v3_get_build_masters_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get build masters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_build_masters_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: type
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_get_build_masters_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

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
            '/v3/builds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v3_get_build_using_get(self, build_master, job, number, **kwargs):  # noqa: E501
        """Get build for build master  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_build_using_get(build_master, job, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :param str job: job (required)
        :param str number: number (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v3_get_build_using_get_with_http_info(build_master, job, number, **kwargs)  # noqa: E501
        else:
            (data) = self.v3_get_build_using_get_with_http_info(build_master, job, number, **kwargs)  # noqa: E501
            return data

    def v3_get_build_using_get_with_http_info(self, build_master, job, number, **kwargs):  # noqa: E501
        """Get build for build master  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_build_using_get_with_http_info(build_master, job, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :param str job: job (required)
        :param str number: number (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_master', 'job', 'number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_get_build_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_master' is set
        if ('build_master' not in params or
                params['build_master'] is None):
            raise ValueError("Missing the required parameter `build_master` when calling `v3_get_build_using_get`")  # noqa: E501
        # verify the required parameter 'job' is set
        if ('job' not in params or
                params['job'] is None):
            raise ValueError("Missing the required parameter `job` when calling `v3_get_build_using_get`")  # noqa: E501
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `v3_get_build_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'build_master' in params:
            path_params['buildMaster'] = params['build_master']  # noqa: E501
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

        query_params = []
        if 'job' in params:
            query_params.append(('job', params['job']))  # noqa: E501

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
            '/v3/builds/{buildMaster}/build/{number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v3_get_builds_using_get(self, build_master, job, **kwargs):  # noqa: E501
        """Get builds for build master  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_builds_using_get(build_master, job, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :param str job: job (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v3_get_builds_using_get_with_http_info(build_master, job, **kwargs)  # noqa: E501
        else:
            (data) = self.v3_get_builds_using_get_with_http_info(build_master, job, **kwargs)  # noqa: E501
            return data

    def v3_get_builds_using_get_with_http_info(self, build_master, job, **kwargs):  # noqa: E501
        """Get builds for build master  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_builds_using_get_with_http_info(build_master, job, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :param str job: job (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_master', 'job']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_get_builds_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_master' is set
        if ('build_master' not in params or
                params['build_master'] is None):
            raise ValueError("Missing the required parameter `build_master` when calling `v3_get_builds_using_get`")  # noqa: E501
        # verify the required parameter 'job' is set
        if ('job' not in params or
                params['job'] is None):
            raise ValueError("Missing the required parameter `job` when calling `v3_get_builds_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'build_master' in params:
            path_params['buildMaster'] = params['build_master']  # noqa: E501

        query_params = []
        if 'job' in params:
            query_params.append(('job', params['job']))  # noqa: E501

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
            '/v3/builds/{buildMaster}/builds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v3_get_job_config_using_get(self, build_master, job, **kwargs):  # noqa: E501
        """Get job config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_job_config_using_get(build_master, job, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :param str job: job (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v3_get_job_config_using_get_with_http_info(build_master, job, **kwargs)  # noqa: E501
        else:
            (data) = self.v3_get_job_config_using_get_with_http_info(build_master, job, **kwargs)  # noqa: E501
            return data

    def v3_get_job_config_using_get_with_http_info(self, build_master, job, **kwargs):  # noqa: E501
        """Get job config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_job_config_using_get_with_http_info(build_master, job, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :param str job: job (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_master', 'job']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_get_job_config_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_master' is set
        if ('build_master' not in params or
                params['build_master'] is None):
            raise ValueError("Missing the required parameter `build_master` when calling `v3_get_job_config_using_get`")  # noqa: E501
        # verify the required parameter 'job' is set
        if ('job' not in params or
                params['job'] is None):
            raise ValueError("Missing the required parameter `job` when calling `v3_get_job_config_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'build_master' in params:
            path_params['buildMaster'] = params['build_master']  # noqa: E501

        query_params = []
        if 'job' in params:
            query_params.append(('job', params['job']))  # noqa: E501

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
            '/v3/builds/{buildMaster}/job', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v3_get_jobs_for_build_master_using_get(self, build_master, **kwargs):  # noqa: E501
        """Get jobs for build master  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_jobs_for_build_master_using_get(build_master, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v3_get_jobs_for_build_master_using_get_with_http_info(build_master, **kwargs)  # noqa: E501
        else:
            (data) = self.v3_get_jobs_for_build_master_using_get_with_http_info(build_master, **kwargs)  # noqa: E501
            return data

    def v3_get_jobs_for_build_master_using_get_with_http_info(self, build_master, **kwargs):  # noqa: E501
        """Get jobs for build master  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_get_jobs_for_build_master_using_get_with_http_info(build_master, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str build_master: buildMaster (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_master']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_get_jobs_for_build_master_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_master' is set
        if ('build_master' not in params or
                params['build_master'] is None):
            raise ValueError("Missing the required parameter `build_master` when calling `v3_get_jobs_for_build_master_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'build_master' in params:
            path_params['buildMaster'] = params['build_master']  # noqa: E501

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
            '/v3/builds/{buildMaster}/jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)