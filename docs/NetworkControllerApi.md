# spinnaker_client.NetworkControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_cloud_provider_using_get**](NetworkControllerApi.md#all_by_cloud_provider_using_get) | **GET** /networks/{cloudProvider} | Retrieve a list of networks for a given cloud provider
[**all_using_get2**](NetworkControllerApi.md#all_using_get2) | **GET** /networks | Retrieve a list of networks, grouped by cloud provider


# **all_by_cloud_provider_using_get**
> list[object] all_by_cloud_provider_using_get(cloud_provider, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of networks for a given cloud provider

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.NetworkControllerApi()
cloud_provider = 'cloud_provider_example' # str | cloudProvider
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of networks for a given cloud provider
    api_response = api_instance.all_by_cloud_provider_using_get(cloud_provider, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkControllerApi->all_by_cloud_provider_using_get: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_using_get2**
> dict(str, object) all_using_get2(x_rate_limit_app=x_rate_limit_app)

Retrieve a list of networks, grouped by cloud provider

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.NetworkControllerApi()
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of networks, grouped by cloud provider
    api_response = api_instance.all_using_get2(x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkControllerApi->all_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

