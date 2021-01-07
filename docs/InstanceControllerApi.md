# spinnaker-python-client.InstanceControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_console_output_using_get**](InstanceControllerApi.md#get_console_output_using_get) | **GET** /instances/{account}/{region}/{instanceId}/console | Retrieve an instance&#39;s console output
[**get_instance_details_using_get**](InstanceControllerApi.md#get_instance_details_using_get) | **GET** /instances/{account}/{region}/{instanceId} | Retrieve an instance&#39;s details


# **get_console_output_using_get**
> object get_console_output_using_get(account, instance_id, region, x_rate_limit_app=x_rate_limit_app, provider=provider)

Retrieve an instance's console output

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.InstanceControllerApi()
account = 'account_example' # str | account
instance_id = 'instance_id_example' # str | instanceId
region = 'region_example' # str | region
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
provider = 'aws' # str | provider (optional) (default to aws)

try:
    # Retrieve an instance's console output
    api_response = api_instance.get_console_output_using_get(account, instance_id, region, x_rate_limit_app=x_rate_limit_app, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceControllerApi->get_console_output_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **instance_id** | **str**| instanceId | 
 **region** | **str**| region | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **provider** | **str**| provider | [optional] [default to aws]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_details_using_get**
> object get_instance_details_using_get(account, instance_id, region, x_rate_limit_app=x_rate_limit_app)

Retrieve an instance's details

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.InstanceControllerApi()
account = 'account_example' # str | account
instance_id = 'instance_id_example' # str | instanceId
region = 'region_example' # str | region
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve an instance's details
    api_response = api_instance.get_instance_details_using_get(account, instance_id, region, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceControllerApi->get_instance_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **instance_id** | **str**| instanceId | 
 **region** | **str**| region | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

