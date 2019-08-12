# swagger_client.EcsServerGroupEventsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events_using_get**](EcsServerGroupEventsControllerApi.md#get_events_using_get) | **GET** /applications/{application}/serverGroups/{account}/{serverGroupName}/events | Retrieves a list of events for a server group


# **get_events_using_get**
> list[object] get_events_using_get(application, account, server_group_name, region, provider)

Retrieves a list of events for a server group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcsServerGroupEventsControllerApi()
application = 'application_example' # str | application
account = 'account_example' # str | account
server_group_name = 'server_group_name_example' # str | serverGroupName
region = 'region_example' # str | region
provider = 'provider_example' # str | provider

try:
    # Retrieves a list of events for a server group
    api_response = api_instance.get_events_using_get(application, account, server_group_name, region, provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcsServerGroupEventsControllerApi->get_events_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **account** | **str**| account | 
 **server_group_name** | **str**| serverGroupName | 
 **region** | **str**| region | 
 **provider** | **str**| provider | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

