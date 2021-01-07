# spinnaker_client.JobControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_using_get**](JobControllerApi.md#get_job_using_get) | **GET** /applications/{applicationName}/jobs/{account}/{region}/{name} | Get job


# **get_job_using_get**
> dict(str, object) get_job_using_get(account, application_name, name, region, x_rate_limit_app=x_rate_limit_app, expand=expand)

Get job

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.JobControllerApi()
account = 'account_example' # str | account
application_name = 'application_name_example' # str | applicationName
name = 'name_example' # str | name
region = 'region_example' # str | region
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
expand = 'false' # str | expand (optional) (default to false)

try:
    # Get job
    api_response = api_instance.get_job_using_get(account, application_name, name, region, x_rate_limit_app=x_rate_limit_app, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobControllerApi->get_job_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application_name** | **str**| applicationName | 
 **name** | **str**| name | 
 **region** | **str**| region | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **expand** | **str**| expand | [optional] [default to false]

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

