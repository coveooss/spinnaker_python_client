# swagger_client.ServerGroupControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_group_details_using_get**](ServerGroupControllerApi.md#get_server_group_details_using_get) | **GET** /applications/{applicationName}/serverGroups/{account}/{region}/{serverGroupName} | Retrieve a server group&#39;s details
[**get_server_groups_for_application_using_get**](ServerGroupControllerApi.md#get_server_groups_for_application_using_get) | **GET** /applications/{applicationName}/serverGroups | Retrieve a list of server groups for a given application


# **get_server_group_details_using_get**
> object get_server_group_details_using_get(application_name, account, region, server_group_name, x_rate_limit_app=x_rate_limit_app, include_details=include_details)

Retrieve a server group's details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerGroupControllerApi()
application_name = 'application_name_example' # str | applicationName
account = 'account_example' # str | account
region = 'region_example' # str | region
server_group_name = 'server_group_name_example' # str | serverGroupName
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
include_details = 'true' # str | includeDetails (optional) (default to true)

try:
    # Retrieve a server group's details
    api_response = api_instance.get_server_group_details_using_get(application_name, account, region, server_group_name, x_rate_limit_app=x_rate_limit_app, include_details=include_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerGroupControllerApi->get_server_group_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| applicationName | 
 **account** | **str**| account | 
 **region** | **str**| region | 
 **server_group_name** | **str**| serverGroupName | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **include_details** | **str**| includeDetails | [optional] [default to true]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_groups_for_application_using_get**
> list[object] get_server_groups_for_application_using_get(application_name, expand=expand, cloud_provider=cloud_provider, clusters=clusters, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of server groups for a given application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerGroupControllerApi()
application_name = 'application_name_example' # str | applicationName
expand = 'false' # str | expand (optional) (default to false)
cloud_provider = 'cloud_provider_example' # str | cloudProvider (optional)
clusters = 'clusters_example' # str | clusters (optional)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of server groups for a given application
    api_response = api_instance.get_server_groups_for_application_using_get(application_name, expand=expand, cloud_provider=cloud_provider, clusters=clusters, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerGroupControllerApi->get_server_groups_for_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| applicationName | 
 **expand** | **str**| expand | [optional] [default to false]
 **cloud_provider** | **str**| cloudProvider | [optional] 
 **clusters** | **str**| clusters | [optional] 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

