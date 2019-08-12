# swagger_client.PipelineConfigControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_pipeline_config_to_pipeline_template_using_get**](PipelineConfigControllerApi.md#convert_pipeline_config_to_pipeline_template_using_get) | **GET** /pipelineConfigs/{pipelineConfigId}/convertToTemplate | Convert a pipeline config to a pipeline template.
[**get_all_pipeline_configs_using_get**](PipelineConfigControllerApi.md#get_all_pipeline_configs_using_get) | **GET** /pipelineConfigs | Get all pipeline configs.
[**get_pipeline_config_history_using_get**](PipelineConfigControllerApi.md#get_pipeline_config_history_using_get) | **GET** /pipelineConfigs/{pipelineConfigId}/history | Get pipeline config history.


# **convert_pipeline_config_to_pipeline_template_using_get**
> str convert_pipeline_config_to_pipeline_template_using_get(pipeline_config_id)

Convert a pipeline config to a pipeline template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineConfigControllerApi()
pipeline_config_id = 'pipeline_config_id_example' # str | pipelineConfigId

try:
    # Convert a pipeline config to a pipeline template.
    api_response = api_instance.convert_pipeline_config_to_pipeline_template_using_get(pipeline_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineConfigControllerApi->convert_pipeline_config_to_pipeline_template_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_config_id** | **str**| pipelineConfigId | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pipeline_configs_using_get**
> list[object] get_all_pipeline_configs_using_get()

Get all pipeline configs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineConfigControllerApi()

try:
    # Get all pipeline configs.
    api_response = api_instance.get_all_pipeline_configs_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineConfigControllerApi->get_all_pipeline_configs_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_config_history_using_get**
> list[object] get_pipeline_config_history_using_get(pipeline_config_id, limit=limit)

Get pipeline config history.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineConfigControllerApi()
pipeline_config_id = 'pipeline_config_id_example' # str | pipelineConfigId
limit = 20 # int | limit (optional) (default to 20)

try:
    # Get pipeline config history.
    api_response = api_instance.get_pipeline_config_history_using_get(pipeline_config_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineConfigControllerApi->get_pipeline_config_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_config_id** | **str**| pipelineConfigId | 
 **limit** | **int**| limit | [optional] [default to 20]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

