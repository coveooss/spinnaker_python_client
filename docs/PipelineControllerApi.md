# swagger_client.PipelineControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_pipeline_using_put1**](PipelineControllerApi.md#cancel_pipeline_using_put1) | **PUT** /pipelines/{id}/cancel | Cancel a pipeline execution
[**delete_pipeline_using_delete**](PipelineControllerApi.md#delete_pipeline_using_delete) | **DELETE** /pipelines/{application}/{pipelineName} | Delete a pipeline definition
[**delete_pipeline_using_delete1**](PipelineControllerApi.md#delete_pipeline_using_delete1) | **DELETE** /pipelines/{id} | Delete a pipeline execution
[**evaluate_expression_for_execution_using_delete**](PipelineControllerApi.md#evaluate_expression_for_execution_using_delete) | **DELETE** /pipelines/{id}/evaluateExpression | Evaluate a pipeline expression using the provided execution as context
[**evaluate_expression_for_execution_using_get**](PipelineControllerApi.md#evaluate_expression_for_execution_using_get) | **GET** /pipelines/{id}/evaluateExpression | Evaluate a pipeline expression using the provided execution as context
[**evaluate_expression_for_execution_using_head**](PipelineControllerApi.md#evaluate_expression_for_execution_using_head) | **HEAD** /pipelines/{id}/evaluateExpression | Evaluate a pipeline expression using the provided execution as context
[**evaluate_expression_for_execution_using_options**](PipelineControllerApi.md#evaluate_expression_for_execution_using_options) | **OPTIONS** /pipelines/{id}/evaluateExpression | Evaluate a pipeline expression using the provided execution as context
[**evaluate_expression_for_execution_using_patch**](PipelineControllerApi.md#evaluate_expression_for_execution_using_patch) | **PATCH** /pipelines/{id}/evaluateExpression | Evaluate a pipeline expression using the provided execution as context
[**evaluate_expression_for_execution_using_post**](PipelineControllerApi.md#evaluate_expression_for_execution_using_post) | **POST** /pipelines/{id}/evaluateExpression | Evaluate a pipeline expression using the provided execution as context
[**evaluate_expression_for_execution_using_put**](PipelineControllerApi.md#evaluate_expression_for_execution_using_put) | **PUT** /pipelines/{id}/evaluateExpression | Evaluate a pipeline expression using the provided execution as context
[**get_pipeline_logs_using_get**](PipelineControllerApi.md#get_pipeline_logs_using_get) | **GET** /pipelines/{id}/logs | Retrieve pipeline execution logs
[**get_pipeline_using_get**](PipelineControllerApi.md#get_pipeline_using_get) | **GET** /pipelines/{id} | Retrieve a pipeline execution
[**invoke_pipeline_config_using_post1**](PipelineControllerApi.md#invoke_pipeline_config_using_post1) | **POST** /pipelines/{application}/{pipelineNameOrId} | Trigger a pipeline execution
[**invoke_pipeline_config_via_echo_using_post**](PipelineControllerApi.md#invoke_pipeline_config_via_echo_using_post) | **POST** /pipelines/v2/{application}/{pipelineNameOrId} | Trigger a pipeline execution
[**pause_pipeline_using_put**](PipelineControllerApi.md#pause_pipeline_using_put) | **PUT** /pipelines/{id}/pause | Pause a pipeline execution
[**rename_pipeline_using_post**](PipelineControllerApi.md#rename_pipeline_using_post) | **POST** /pipelines/move | Rename a pipeline definition
[**restart_stage_using_put**](PipelineControllerApi.md#restart_stage_using_put) | **PUT** /pipelines/{id}/stages/{stageId}/restart | Restart a stage execution
[**resume_pipeline_using_put**](PipelineControllerApi.md#resume_pipeline_using_put) | **PUT** /pipelines/{id}/resume | Resume a pipeline execution
[**save_pipeline_using_post**](PipelineControllerApi.md#save_pipeline_using_post) | **POST** /pipelines | Save a pipeline definition
[**start_using_post**](PipelineControllerApi.md#start_using_post) | **POST** /pipelines/start | Initiate a pipeline execution
[**update_pipeline_using_put**](PipelineControllerApi.md#update_pipeline_using_put) | **PUT** /pipelines/{id} | Update a pipeline definition
[**update_stage_using_patch**](PipelineControllerApi.md#update_stage_using_patch) | **PATCH** /pipelines/{id}/stages/{stageId} | Update a stage execution


# **cancel_pipeline_using_put1**
> cancel_pipeline_using_put1(id, reason=reason, force=force)

Cancel a pipeline execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
reason = 'reason_example' # str | reason (optional)
force = false # bool | force (optional) (default to false)

try:
    # Cancel a pipeline execution
    api_instance.cancel_pipeline_using_put1(id, reason=reason, force=force)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->cancel_pipeline_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **reason** | **str**| reason | [optional] 
 **force** | **bool**| force | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline_using_delete**
> delete_pipeline_using_delete(application, pipeline_name)

Delete a pipeline definition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
application = 'application_example' # str | application
pipeline_name = 'pipeline_name_example' # str | pipelineName

try:
    # Delete a pipeline definition
    api_instance.delete_pipeline_using_delete(application, pipeline_name)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->delete_pipeline_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **pipeline_name** | **str**| pipelineName | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline_using_delete1**
> dict(str, object) delete_pipeline_using_delete1(id)

Delete a pipeline execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id

try:
    # Delete a pipeline execution
    api_response = api_instance.delete_pipeline_using_delete1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->delete_pipeline_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_expression_for_execution_using_delete**
> dict(str, object) evaluate_expression_for_execution_using_delete(id, expression)

Evaluate a pipeline expression using the provided execution as context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
expression = 'expression_example' # str | expression

try:
    # Evaluate a pipeline expression using the provided execution as context
    api_response = api_instance.evaluate_expression_for_execution_using_delete(id, expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->evaluate_expression_for_execution_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **expression** | **str**| expression | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_expression_for_execution_using_get**
> dict(str, object) evaluate_expression_for_execution_using_get(id, expression)

Evaluate a pipeline expression using the provided execution as context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
expression = 'expression_example' # str | expression

try:
    # Evaluate a pipeline expression using the provided execution as context
    api_response = api_instance.evaluate_expression_for_execution_using_get(id, expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->evaluate_expression_for_execution_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **expression** | **str**| expression | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_expression_for_execution_using_head**
> dict(str, object) evaluate_expression_for_execution_using_head(id, expression)

Evaluate a pipeline expression using the provided execution as context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
expression = 'expression_example' # str | expression

try:
    # Evaluate a pipeline expression using the provided execution as context
    api_response = api_instance.evaluate_expression_for_execution_using_head(id, expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->evaluate_expression_for_execution_using_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **expression** | **str**| expression | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_expression_for_execution_using_options**
> dict(str, object) evaluate_expression_for_execution_using_options(id, expression)

Evaluate a pipeline expression using the provided execution as context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
expression = 'expression_example' # str | expression

try:
    # Evaluate a pipeline expression using the provided execution as context
    api_response = api_instance.evaluate_expression_for_execution_using_options(id, expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->evaluate_expression_for_execution_using_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **expression** | **str**| expression | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_expression_for_execution_using_patch**
> dict(str, object) evaluate_expression_for_execution_using_patch(id, expression)

Evaluate a pipeline expression using the provided execution as context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
expression = 'expression_example' # str | expression

try:
    # Evaluate a pipeline expression using the provided execution as context
    api_response = api_instance.evaluate_expression_for_execution_using_patch(id, expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->evaluate_expression_for_execution_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **expression** | **str**| expression | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_expression_for_execution_using_post**
> dict(str, object) evaluate_expression_for_execution_using_post(id, expression)

Evaluate a pipeline expression using the provided execution as context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
expression = 'expression_example' # str | expression

try:
    # Evaluate a pipeline expression using the provided execution as context
    api_response = api_instance.evaluate_expression_for_execution_using_post(id, expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->evaluate_expression_for_execution_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **expression** | **str**| expression | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_expression_for_execution_using_put**
> dict(str, object) evaluate_expression_for_execution_using_put(id, expression)

Evaluate a pipeline expression using the provided execution as context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
expression = 'expression_example' # str | expression

try:
    # Evaluate a pipeline expression using the provided execution as context
    api_response = api_instance.evaluate_expression_for_execution_using_put(id, expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->evaluate_expression_for_execution_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **expression** | **str**| expression | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_logs_using_get**
> list[object] get_pipeline_logs_using_get(id)

Retrieve pipeline execution logs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id

try:
    # Retrieve pipeline execution logs
    api_response = api_instance.get_pipeline_logs_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->get_pipeline_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_using_get**
> object get_pipeline_using_get(id)

Retrieve a pipeline execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id

try:
    # Retrieve a pipeline execution
    api_response = api_instance.get_pipeline_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->get_pipeline_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_pipeline_config_using_post1**
> HttpEntity invoke_pipeline_config_using_post1(application, pipeline_name_or_id, trigger=trigger)

Trigger a pipeline execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
application = 'application_example' # str | application
pipeline_name_or_id = 'pipeline_name_or_id_example' # str | pipelineNameOrId
trigger = NULL # object | trigger (optional)

try:
    # Trigger a pipeline execution
    api_response = api_instance.invoke_pipeline_config_using_post1(application, pipeline_name_or_id, trigger=trigger)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->invoke_pipeline_config_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **pipeline_name_or_id** | **str**| pipelineNameOrId | 
 **trigger** | **object**| trigger | [optional] 

### Return type

[**HttpEntity**](HttpEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_pipeline_config_via_echo_using_post**
> HttpEntity invoke_pipeline_config_via_echo_using_post(application, pipeline_name_or_id, trigger=trigger)

Trigger a pipeline execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
application = 'application_example' # str | application
pipeline_name_or_id = 'pipeline_name_or_id_example' # str | pipelineNameOrId
trigger = NULL # object | trigger (optional)

try:
    # Trigger a pipeline execution
    api_response = api_instance.invoke_pipeline_config_via_echo_using_post(application, pipeline_name_or_id, trigger=trigger)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->invoke_pipeline_config_via_echo_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **pipeline_name_or_id** | **str**| pipelineNameOrId | 
 **trigger** | **object**| trigger | [optional] 

### Return type

[**HttpEntity**](HttpEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_pipeline_using_put**
> pause_pipeline_using_put(id)

Pause a pipeline execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id

try:
    # Pause a pipeline execution
    api_instance.pause_pipeline_using_put(id)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->pause_pipeline_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_pipeline_using_post**
> rename_pipeline_using_post(rename_command)

Rename a pipeline definition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
rename_command = NULL # object | renameCommand

try:
    # Rename a pipeline definition
    api_instance.rename_pipeline_using_post(rename_command)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->rename_pipeline_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rename_command** | **object**| renameCommand | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_stage_using_put**
> dict(str, object) restart_stage_using_put(id, stage_id, context)

Restart a stage execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
stage_id = 'stage_id_example' # str | stageId
context = NULL # object | context

try:
    # Restart a stage execution
    api_response = api_instance.restart_stage_using_put(id, stage_id, context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->restart_stage_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **stage_id** | **str**| stageId | 
 **context** | **object**| context | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_pipeline_using_put**
> dict(str, object) resume_pipeline_using_put(id)

Resume a pipeline execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id

try:
    # Resume a pipeline execution
    api_response = api_instance.resume_pipeline_using_put(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->resume_pipeline_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_pipeline_using_post**
> save_pipeline_using_post(pipeline)

Save a pipeline definition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
pipeline = NULL # object | pipeline

try:
    # Save a pipeline definition
    api_instance.save_pipeline_using_post(pipeline)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->save_pipeline_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | **object**| pipeline | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_using_post**
> ResponseEntity start_using_post(map)

Initiate a pipeline execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
map = NULL # object | map

try:
    # Initiate a pipeline execution
    api_response = api_instance.start_using_post(map)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->start_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map** | **object**| map | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline_using_put**
> dict(str, object) update_pipeline_using_put(id, pipeline)

Update a pipeline definition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
pipeline = NULL # object | pipeline

try:
    # Update a pipeline definition
    api_response = api_instance.update_pipeline_using_put(id, pipeline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->update_pipeline_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **pipeline** | **object**| pipeline | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stage_using_patch**
> dict(str, object) update_stage_using_patch(id, stage_id, context)

Update a stage execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PipelineControllerApi()
id = 'id_example' # str | id
stage_id = 'stage_id_example' # str | stageId
context = NULL # object | context

try:
    # Update a stage execution
    api_response = api_instance.update_stage_using_patch(id, stage_id, context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineControllerApi->update_stage_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **stage_id** | **str**| stageId | 
 **context** | **object**| context | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

