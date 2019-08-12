# swagger_client.SubnetControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_cloud_provider_using_get1**](SubnetControllerApi.md#all_by_cloud_provider_using_get1) | **GET** /subnets/{cloudProvider} | Retrieve a list of subnets for a given cloud provider


# **all_by_cloud_provider_using_get1**
> list[object] all_by_cloud_provider_using_get1(cloud_provider, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of subnets for a given cloud provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubnetControllerApi()
cloud_provider = 'cloud_provider_example' # str | cloudProvider
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of subnets for a given cloud provider
    api_response = api_instance.all_by_cloud_provider_using_get1(cloud_provider, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubnetControllerApi->all_by_cloud_provider_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_provider** | **str**| cloudProvider | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

