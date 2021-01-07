# spinnaker-python-client.AmazonInfrastructureControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_functions_using_get**](AmazonInfrastructureControllerApi.md#application_functions_using_get) | **GET** /applications/{application}/functions | Get application functions
[**functions_using_get**](AmazonInfrastructureControllerApi.md#functions_using_get) | **GET** /functions | Get functions
[**instance_types_using_get**](AmazonInfrastructureControllerApi.md#instance_types_using_get) | **GET** /instanceTypes | Get instance types
[**subnets_using_get**](AmazonInfrastructureControllerApi.md#subnets_using_get) | **GET** /subnets | Get subnets
[**vpcs_using_get**](AmazonInfrastructureControllerApi.md#vpcs_using_get) | **GET** /vpcs | Get VPCs


# **application_functions_using_get**
> list[object] application_functions_using_get(application)

Get application functions

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.AmazonInfrastructureControllerApi()
application = 'application_example' # str | application

try:
    # Get application functions
    api_response = api_instance.application_functions_using_get(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmazonInfrastructureControllerApi->application_functions_using_get: %s\n" % e)
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

# **functions_using_get**
> list[object] functions_using_get(account=account, function_name=function_name, region=region)

Get functions

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.AmazonInfrastructureControllerApi()
account = 'account_example' # str | account (optional)
function_name = 'function_name_example' # str | functionName (optional)
region = 'region_example' # str | region (optional)

try:
    # Get functions
    api_response = api_instance.functions_using_get(account=account, function_name=function_name, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmazonInfrastructureControllerApi->functions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | [optional] 
 **function_name** | **str**| functionName | [optional] 
 **region** | **str**| region | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_types_using_get**
> list[object] instance_types_using_get()

Get instance types

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.AmazonInfrastructureControllerApi()

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

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subnets_using_get**
> list[object] subnets_using_get()

Get subnets

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.AmazonInfrastructureControllerApi()

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

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vpcs_using_get**
> list[object] vpcs_using_get()

Get VPCs

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.AmazonInfrastructureControllerApi()

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

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

