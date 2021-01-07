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


class DeckPluginsControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_plugin_asset_using_get(self, asset, plugin_id, plugin_version, **kwargs):  # noqa: E501
        """Retrieve a single plugin asset by version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plugin_asset_using_get(asset, plugin_id, plugin_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset: asset (required)
        :param str plugin_id: pluginId (required)
        :param str plugin_version: pluginVersion (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_plugin_asset_using_get_with_http_info(asset, plugin_id, plugin_version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_plugin_asset_using_get_with_http_info(asset, plugin_id, plugin_version, **kwargs)  # noqa: E501
            return data

    def get_plugin_asset_using_get_with_http_info(self, asset, plugin_id, plugin_version, **kwargs):  # noqa: E501
        """Retrieve a single plugin asset by version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plugin_asset_using_get_with_http_info(asset, plugin_id, plugin_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset: asset (required)
        :param str plugin_id: pluginId (required)
        :param str plugin_version: pluginVersion (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset', 'plugin_id', 'plugin_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_plugin_asset_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset' is set
        if ('asset' not in params or
                params['asset'] is None):
            raise ValueError("Missing the required parameter `asset` when calling `get_plugin_asset_using_get`")  # noqa: E501
        # verify the required parameter 'plugin_id' is set
        if ('plugin_id' not in params or
                params['plugin_id'] is None):
            raise ValueError("Missing the required parameter `plugin_id` when calling `get_plugin_asset_using_get`")  # noqa: E501
        # verify the required parameter 'plugin_version' is set
        if ('plugin_version' not in params or
                params['plugin_version'] is None):
            raise ValueError("Missing the required parameter `plugin_version` when calling `get_plugin_asset_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset' in params:
            path_params['asset'] = params['asset']  # noqa: E501
        if 'plugin_id' in params:
            path_params['pluginId'] = params['plugin_id']  # noqa: E501
        if 'plugin_version' in params:
            path_params['pluginVersion'] = params['plugin_version']  # noqa: E501

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
            '/plugins/deck/{pluginId}/{pluginVersion}/{asset}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_plugin_manifest_using_get(self, **kwargs):  # noqa: E501
        """Retrieve a plugin manifest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plugin_manifest_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DeckPluginVersion]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_plugin_manifest_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_plugin_manifest_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_plugin_manifest_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a plugin manifest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plugin_manifest_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DeckPluginVersion]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_plugin_manifest_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/plugins/deck/plugin-manifest.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeckPluginVersion]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
