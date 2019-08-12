# swagger_client.SearchControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_using_get**](SearchControllerApi.md#search_using_get) | **GET** /search | Search infrastructure


# **search_using_get**
> list[object] search_using_get(type, q=q, platform=platform, page_size=page_size, page=page, allow_short_query=allow_short_query, x_rate_limit_app=x_rate_limit_app)

Search infrastructure

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchControllerApi()
type = 'type_example' # str | type
q = 'q_example' # str | q (optional)
platform = 'platform_example' # str | platform (optional)
page_size = 10000 # int | pageSize (optional) (default to 10000)
page = 1 # int | page (optional) (default to 1)
allow_short_query = false # bool | allowShortQuery (optional) (default to false)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Search infrastructure
    api_response = api_instance.search_using_get(type, q=q, platform=platform, page_size=page_size, page=page, allow_short_query=allow_short_query, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchControllerApi->search_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **q** | **str**| q | [optional] 
 **platform** | **str**| platform | [optional] 
 **page_size** | **int**| pageSize | [optional] [default to 10000]
 **page** | **int**| page | [optional] [default to 1]
 **allow_short_query** | **bool**| allowShortQuery | [optional] [default to false]
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

