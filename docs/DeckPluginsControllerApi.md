# spinnaker-python-client.DeckPluginsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plugin_asset_using_get**](DeckPluginsControllerApi.md#get_plugin_asset_using_get) | **GET** /plugins/deck/{pluginId}/{pluginVersion}/{asset} | Retrieve a single plugin asset by version
[**get_plugin_manifest_using_get**](DeckPluginsControllerApi.md#get_plugin_manifest_using_get) | **GET** /plugins/deck/plugin-manifest.json | Retrieve a plugin manifest


# **get_plugin_asset_using_get**
> str get_plugin_asset_using_get(asset, plugin_id, plugin_version)

Retrieve a single plugin asset by version

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.DeckPluginsControllerApi()
asset = 'asset_example' # str | asset
plugin_id = 'plugin_id_example' # str | pluginId
plugin_version = 'plugin_version_example' # str | pluginVersion

try:
    # Retrieve a single plugin asset by version
    api_response = api_instance.get_plugin_asset_using_get(asset, plugin_id, plugin_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeckPluginsControllerApi->get_plugin_asset_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| asset | 
 **plugin_id** | **str**| pluginId | 
 **plugin_version** | **str**| pluginVersion | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_manifest_using_get**
> list[DeckPluginVersion] get_plugin_manifest_using_get()

Retrieve a plugin manifest

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.DeckPluginsControllerApi()

try:
    # Retrieve a plugin manifest
    api_response = api_instance.get_plugin_manifest_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeckPluginsControllerApi->get_plugin_manifest_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DeckPluginVersion]**](DeckPluginVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

