# swagger_client.VersionControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version_using_get**](VersionControllerApi.md#get_version_using_get) | **GET** /version | Fetch Gate&#39;s current version


# **get_version_using_get**
> Version get_version_using_get()

Fetch Gate's current version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionControllerApi()

try:
    # Fetch Gate's current version
    api_response = api_instance.get_version_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionControllerApi->get_version_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

