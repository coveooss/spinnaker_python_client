# swagger_client.JobControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_using_get**](JobControllerApi.md#get_job_using_get) | **GET** /applications/{applicationName}/jobs/{account}/{region}/{name} | Get job


# **get_job_using_get**
> dict(str, object) get_job_using_get(application_name, account, region, name, expand=expand, x_rate_limit_app=x_rate_limit_app)

Get job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobControllerApi()
application_name = 'application_name_example' # str | applicationName
account = 'account_example' # str | account
region = 'region_example' # str | region
name = 'name_example' # str | name
expand = 'false' # str | expand (optional) (default to false)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Get job
    api_response = api_instance.get_job_using_get(application_name, account, region, name, expand=expand, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobControllerApi->get_job_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| applicationName | 
 **account** | **str**| account | 
 **region** | **str**| region | 
 **name** | **str**| name | 
 **expand** | **str**| expand | [optional] [default to false]
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

