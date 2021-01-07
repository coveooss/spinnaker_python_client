# spinnaker-python-client.RawResourceControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_raw_resources_using_get**](RawResourceControllerApi.md#get_application_raw_resources_using_get) | **GET** /applications/{application}/rawResources | Retrieve a list of raw resources for a given application


# **get_application_raw_resources_using_get**
> list[object] get_application_raw_resources_using_get(application)

Retrieve a list of raw resources for a given application

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.RawResourceControllerApi()
application = 'application_example' # str | application

try:
    # Retrieve a list of raw resources for a given application
    api_response = api_instance.get_application_raw_resources_using_get(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawResourceControllerApi->get_application_raw_resources_using_get: %s\n" % e)
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

