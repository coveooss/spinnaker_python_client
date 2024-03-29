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

from spinnaker_swagger_client.api_client import ApiClient


class V2CanaryConfigControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_canary_config_using_post(self, config, **kwargs):  # noqa: E501
        """Create a canary configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_canary_config_using_post(config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object config: config (required)
        :param str configuration_account_name: configurationAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_canary_config_using_post_with_http_info(config, **kwargs)  # noqa: E501
        else:
            (data) = self.create_canary_config_using_post_with_http_info(config, **kwargs)  # noqa: E501
            return data

    def create_canary_config_using_post_with_http_info(self, config, **kwargs):  # noqa: E501
        """Create a canary configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_canary_config_using_post_with_http_info(config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object config: config (required)
        :param str configuration_account_name: configurationAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['config', 'configuration_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_canary_config_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config' is set
        if ('config' not in params or
                params['config'] is None):
            raise ValueError("Missing the required parameter `config` when calling `create_canary_config_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'configuration_account_name' in params:
            query_params.append(('configurationAccountName', params['configuration_account_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'config' in params:
            body_params = params['config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2/canaryConfig', 'POST',
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

    def delete_canary_config_using_delete(self, id, **kwargs):  # noqa: E501
        """Delete a canary configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_canary_config_using_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :param str configuration_account_name: configurationAccountName
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_canary_config_using_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_canary_config_using_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_canary_config_using_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a canary configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_canary_config_using_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :param str configuration_account_name: configurationAccountName
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'configuration_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_canary_config_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_canary_config_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'configuration_account_name' in params:
            query_params.append(('configurationAccountName', params['configuration_account_name']))  # noqa: E501

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
            '/v2/canaryConfig/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_canary_config_using_get(self, id, **kwargs):  # noqa: E501
        """Retrieve a canary configuration by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canary_config_using_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :param str configuration_account_name: configurationAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_canary_config_using_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_canary_config_using_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_canary_config_using_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a canary configuration by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canary_config_using_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :param str configuration_account_name: configurationAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'configuration_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_canary_config_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_canary_config_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'configuration_account_name' in params:
            query_params.append(('configurationAccountName', params['configuration_account_name']))  # noqa: E501

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
            '/v2/canaryConfig/{id}', 'GET',
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

    def get_canary_configs_using_get(self, **kwargs):  # noqa: E501
        """Retrieve a list of canary configurations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canary_configs_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: application
        :param str configuration_account_name: configurationAccountName
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_canary_configs_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_canary_configs_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_canary_configs_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of canary configurations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canary_configs_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: application
        :param str configuration_account_name: configurationAccountName
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application', 'configuration_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_canary_configs_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'application' in params:
            query_params.append(('application', params['application']))  # noqa: E501
        if 'configuration_account_name' in params:
            query_params.append(('configurationAccountName', params['configuration_account_name']))  # noqa: E501

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
            '/v2/canaryConfig', 'GET',
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

    def update_canary_config_using_put(self, config, id, **kwargs):  # noqa: E501
        """Update a canary configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_canary_config_using_put(config, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object config: config (required)
        :param str id: id (required)
        :param str configuration_account_name: configurationAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_canary_config_using_put_with_http_info(config, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_canary_config_using_put_with_http_info(config, id, **kwargs)  # noqa: E501
            return data

    def update_canary_config_using_put_with_http_info(self, config, id, **kwargs):  # noqa: E501
        """Update a canary configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_canary_config_using_put_with_http_info(config, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object config: config (required)
        :param str id: id (required)
        :param str configuration_account_name: configurationAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['config', 'id', 'configuration_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_canary_config_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config' is set
        if ('config' not in params or
                params['config'] is None):
            raise ValueError("Missing the required parameter `config` when calling `update_canary_config_using_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_canary_config_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'configuration_account_name' in params:
            query_params.append(('configurationAccountName', params['configuration_account_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'config' in params:
            body_params = params['config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2/canaryConfig/{id}', 'PUT',
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
