# spinnaker_client.BakeControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bake_options_using_get**](BakeControllerApi.md#bake_options_using_get) | **GET** /bakery/options/{cloudProvider} | Retrieve a list of available bakery base images for a given cloud provider
[**bake_options_using_get1**](BakeControllerApi.md#bake_options_using_get1) | **GET** /bakery/options | Retrieve a list of available bakery base images, grouped by cloud provider
[**lookup_logs_using_get**](BakeControllerApi.md#lookup_logs_using_get) | **GET** /bakery/logs/{region}/{statusId} | Retrieve the logs for a given bake


# **bake_options_using_get**
> object bake_options_using_get(cloud_provider)

Retrieve a list of available bakery base images for a given cloud provider

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.BakeControllerApi()
cloud_provider = 'cloud_provider_example' # str | cloudProvider

try:
    # Retrieve a list of available bakery base images for a given cloud provider
    api_response = api_instance.bake_options_using_get(cloud_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BakeControllerApi->bake_options_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_provider** | **str**| cloudProvider | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bake_options_using_get1**
> object bake_options_using_get1()

Retrieve a list of available bakery base images, grouped by cloud provider

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.BakeControllerApi()

try:
    # Retrieve a list of available bakery base images, grouped by cloud provider
    api_response = api_instance.bake_options_using_get1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BakeControllerApi->bake_options_using_get1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_logs_using_get**
> object lookup_logs_using_get(region, status_id)

Retrieve the logs for a given bake

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.BakeControllerApi()
region = 'region_example' # str | region
status_id = 'status_id_example' # str | statusId

try:
    # Retrieve the logs for a given bake
    api_response = api_instance.lookup_logs_using_get(region, status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BakeControllerApi->lookup_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| region | 
 **status_id** | **str**| statusId | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

