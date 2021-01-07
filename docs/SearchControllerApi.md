# spinnaker-python-client.SearchControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_using_get**](SearchControllerApi.md#search_using_get) | **GET** /search | Search infrastructure


# **search_using_get**
> list[object] search_using_get(type, x_rate_limit_app=x_rate_limit_app, allow_short_query=allow_short_query, page=page, page_size=page_size, platform=platform, q=q)

Search infrastructure

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.SearchControllerApi()
type = 'type_example' # str | type
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
allow_short_query = false # bool | allowShortQuery (optional) (default to false)
page = 1 # int | page (optional) (default to 1)
page_size = 10000 # int | pageSize (optional) (default to 10000)
platform = 'platform_example' # str | platform (optional)
q = 'q_example' # str | q (optional)

try:
    # Search infrastructure
    api_response = api_instance.search_using_get(type, x_rate_limit_app=x_rate_limit_app, allow_short_query=allow_short_query, page=page, page_size=page_size, platform=platform, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchControllerApi->search_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **allow_short_query** | **bool**| allowShortQuery | [optional] [default to false]
 **page** | **int**| page | [optional] [default to 1]
 **page_size** | **int**| pageSize | [optional] [default to 10000]
 **platform** | **str**| platform | [optional] 
 **q** | **str**| q | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

