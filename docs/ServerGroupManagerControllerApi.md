# spinnaker_client.ServerGroupManagerControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_group_managers_for_application_using_get**](ServerGroupManagerControllerApi.md#get_server_group_managers_for_application_using_get) | **GET** /applications/{application}/serverGroupManagers | Retrieve a list of server group managers for an application


# **get_server_group_managers_for_application_using_get**
> list[object] get_server_group_managers_for_application_using_get(application)

Retrieve a list of server group managers for an application

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ServerGroupManagerControllerApi()
application = 'application_example' # str | application

try:
    # Retrieve a list of server group managers for an application
    api_response = api_instance.get_server_group_managers_for_application_using_get(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerGroupManagerControllerApi->get_server_group_managers_for_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

