# spinnaker_client.PluginInfoControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_plugin_info_using_delete**](PluginInfoControllerApi.md#delete_plugin_info_using_delete) | **DELETE** /plugins/info/{id} | Delete plugin info with the provided Id
[**get_all_plugin_info_using_get**](PluginInfoControllerApi.md#get_all_plugin_info_using_get) | **GET** /plugins/info | Get all plugin info objects
[**persist_plugin_info_using_post**](PluginInfoControllerApi.md#persist_plugin_info_using_post) | **POST** /plugins/info | Persist plugin metadata information
[**persist_plugin_info_using_put**](PluginInfoControllerApi.md#persist_plugin_info_using_put) | **PUT** /plugins/info | Persist plugin metadata information


# **delete_plugin_info_using_delete**
> object delete_plugin_info_using_delete(id)

Delete plugin info with the provided Id

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.PluginInfoControllerApi()
id = 'id_example' # str | id

try:
    # Delete plugin info with the provided Id
    api_response = api_instance.delete_plugin_info_using_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginInfoControllerApi->delete_plugin_info_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plugin_info_using_get**
> list[object] get_all_plugin_info_using_get(service=service)

Get all plugin info objects

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.PluginInfoControllerApi()
service = 'service_example' # str | service (optional)

try:
    # Get all plugin info objects
    api_response = api_instance.get_all_plugin_info_using_get(service=service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginInfoControllerApi->get_all_plugin_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| service | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persist_plugin_info_using_post**
> persist_plugin_info_using_post(plugin_info)

Persist plugin metadata information

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.PluginInfoControllerApi()
plugin_info = spinnaker_client.SpinnakerPluginInfo() # SpinnakerPluginInfo | pluginInfo

try:
    # Persist plugin metadata information
    api_instance.persist_plugin_info_using_post(plugin_info)
except ApiException as e:
    print("Exception when calling PluginInfoControllerApi->persist_plugin_info_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_info** | [**SpinnakerPluginInfo**](SpinnakerPluginInfo.md)| pluginInfo | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persist_plugin_info_using_put**
> persist_plugin_info_using_put(plugin_info)

Persist plugin metadata information

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.PluginInfoControllerApi()
plugin_info = spinnaker_client.SpinnakerPluginInfo() # SpinnakerPluginInfo | pluginInfo

try:
    # Persist plugin metadata information
    api_instance.persist_plugin_info_using_put(plugin_info)
except ApiException as e:
    print("Exception when calling PluginInfoControllerApi->persist_plugin_info_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_info** | [**SpinnakerPluginInfo**](SpinnakerPluginInfo.md)| pluginInfo | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

