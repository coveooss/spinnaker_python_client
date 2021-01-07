# spinnaker_swagger_client.EcsServerGroupEventsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events_using_get**](EcsServerGroupEventsControllerApi.md#get_events_using_get) | **GET** /applications/{application}/serverGroups/{account}/{serverGroupName}/events | Retrieves a list of events for a server group


# **get_events_using_get**
> list[object] get_events_using_get(account, application, provider, region, server_group_name)

Retrieves a list of events for a server group

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.EcsServerGroupEventsControllerApi()
account = 'account_example' # str | account
application = 'application_example' # str | application
provider = 'provider_example' # str | provider
region = 'region_example' # str | region
server_group_name = 'server_group_name_example' # str | serverGroupName

try:
    # Retrieves a list of events for a server group
    api_response = api_instance.get_events_using_get(account, application, provider, region, server_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcsServerGroupEventsControllerApi->get_events_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application** | **str**| application | 
 **provider** | **str**| provider | 
 **region** | **str**| region | 
 **server_group_name** | **str**| serverGroupName | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

