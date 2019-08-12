# swagger_client.SnapshotControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_snapshot_using_get**](SnapshotControllerApi.md#get_current_snapshot_using_get) | **GET** /applications/{application}/snapshots/{account} | Get current snapshot
[**get_snapshot_history_using_get**](SnapshotControllerApi.md#get_snapshot_history_using_get) | **GET** /applications/{application}/snapshots/{account}/history | Get snapshot history


# **get_current_snapshot_using_get**
> dict(str, object) get_current_snapshot_using_get(application, account)

Get current snapshot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SnapshotControllerApi()
application = 'application_example' # str | application
account = 'account_example' # str | account

try:
    # Get current snapshot
    api_response = api_instance.get_current_snapshot_using_get(application, account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotControllerApi->get_current_snapshot_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **account** | **str**| account | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_history_using_get**
> list[object] get_snapshot_history_using_get(application, account, limit=limit)

Get snapshot history

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SnapshotControllerApi()
application = 'application_example' # str | application
account = 'account_example' # str | account
limit = 20 # int | limit (optional) (default to 20)

try:
    # Get snapshot history
    api_response = api_instance.get_snapshot_history_using_get(application, account, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotControllerApi->get_snapshot_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **account** | **str**| account | 
 **limit** | **int**| limit | [optional] [default to 20]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

