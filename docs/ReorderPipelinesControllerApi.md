# spinnaker_client.ReorderPipelinesControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reorder_pipelines_using_post**](ReorderPipelinesControllerApi.md#reorder_pipelines_using_post) | **POST** /actions/pipelines/reorder | Re-order pipelines


# **reorder_pipelines_using_post**
> object reorder_pipelines_using_post(reorder_pipelines_command)

Re-order pipelines

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ReorderPipelinesControllerApi()
reorder_pipelines_command = spinnaker_client.ReorderPipelinesCommand() # ReorderPipelinesCommand | reorderPipelinesCommand

try:
    # Re-order pipelines
    api_response = api_instance.reorder_pipelines_using_post(reorder_pipelines_command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReorderPipelinesControllerApi->reorder_pipelines_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reorder_pipelines_command** | [**ReorderPipelinesCommand**](ReorderPipelinesCommand.md)| reorderPipelinesCommand | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

