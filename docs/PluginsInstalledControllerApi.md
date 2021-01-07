# spinnaker_swagger_client.PluginsInstalledControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_installed_plugins_using_get**](PluginsInstalledControllerApi.md#get_installed_plugins_using_get) | **GET** /plugins/installed | Get all installed Spinnaker plugins


# **get_installed_plugins_using_get**
> dict(str, list[SpinnakerPluginDescriptor]) get_installed_plugins_using_get(service=service)

Get all installed Spinnaker plugins

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.PluginsInstalledControllerApi()
service = 'service_example' # str | service (optional)

try:
    # Get all installed Spinnaker plugins
    api_response = api_instance.get_installed_plugins_using_get(service=service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsInstalledControllerApi->get_installed_plugins_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| service | [optional] 

### Return type

**dict(str, list[SpinnakerPluginDescriptor])**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

