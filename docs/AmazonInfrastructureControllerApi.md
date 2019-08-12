# swagger_client.AmazonInfrastructureControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_types_using_get**](AmazonInfrastructureControllerApi.md#instance_types_using_get) | **GET** /instanceTypes | Get instance types
[**subnets_using_get**](AmazonInfrastructureControllerApi.md#subnets_using_get) | **GET** /subnets | Get subnets
[**vpcs_using_get**](AmazonInfrastructureControllerApi.md#vpcs_using_get) | **GET** /vpcs | Get VPCs


# **instance_types_using_get**
> list[object] instance_types_using_get()

Get instance types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmazonInfrastructureControllerApi()

try:
    # Get instance types
    api_response = api_instance.instance_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmazonInfrastructureControllerApi->instance_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subnets_using_get**
> list[object] subnets_using_get()

Get subnets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmazonInfrastructureControllerApi()

try:
    # Get subnets
    api_response = api_instance.subnets_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmazonInfrastructureControllerApi->subnets_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vpcs_using_get**
> list[object] vpcs_using_get()

Get VPCs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmazonInfrastructureControllerApi()

try:
    # Get VPCs
    api_response = api_instance.vpcs_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmazonInfrastructureControllerApi->vpcs_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

