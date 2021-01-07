# spinnaker_client.PluginPublishControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publish_plugin_using_post**](PluginPublishControllerApi.md#publish_plugin_using_post) | **POST** /plugins/publish/{pluginId}/{pluginVersion} | Publish a plugin binary and the plugin info metadata.


# **publish_plugin_using_post**
> publish_plugin_using_post(plugin, plugin_id, plugin_info, plugin_version)

Publish a plugin binary and the plugin info metadata.

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.PluginPublishControllerApi()
plugin = '/path/to/file.txt' # file | plugin
plugin_id = 'plugin_id_example' # str | pluginId
plugin_info = NULL # object | pluginInfo
plugin_version = 'plugin_version_example' # str | pluginVersion

try:
    # Publish a plugin binary and the plugin info metadata.
    api_instance.publish_plugin_using_post(plugin, plugin_id, plugin_info, plugin_version)
except ApiException as e:
    print("Exception when calling PluginPublishControllerApi->publish_plugin_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin** | **file**| plugin | 
 **plugin_id** | **str**| pluginId | 
 **plugin_info** | [**object**](.md)| pluginInfo | 
 **plugin_version** | **str**| pluginVersion | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

