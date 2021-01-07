# spinnaker-python-client.SnapshotControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_snapshot_using_get**](SnapshotControllerApi.md#get_current_snapshot_using_get) | **GET** /applications/{application}/snapshots/{account} | Get current snapshot
[**get_snapshot_history_using_get**](SnapshotControllerApi.md#get_snapshot_history_using_get) | **GET** /applications/{application}/snapshots/{account}/history | Get snapshot history


# **get_current_snapshot_using_get**
> dict(str, object) get_current_snapshot_using_get(account, application)

Get current snapshot

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.SnapshotControllerApi()
account = 'account_example' # str | account
application = 'application_example' # str | application

try:
    # Get current snapshot
    api_response = api_instance.get_current_snapshot_using_get(account, application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotControllerApi->get_current_snapshot_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application** | **str**| application | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_history_using_get**
> list[object] get_snapshot_history_using_get(account, application, limit=limit)

Get snapshot history

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.SnapshotControllerApi()
account = 'account_example' # str | account
application = 'application_example' # str | application
limit = 20 # int | limit (optional) (default to 20)

try:
    # Get snapshot history
    api_response = api_instance.get_snapshot_history_using_get(account, application, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotControllerApi->get_snapshot_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application** | **str**| application | 
 **limit** | **int**| limit | [optional] [default to 20]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

