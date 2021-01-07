# spinnaker-python-client.PipelineTemplatesControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post**](PipelineTemplatesControllerApi.md#create_using_post) | **POST** /pipelineTemplates | Create a pipeline template.
[**delete_using_delete**](PipelineTemplatesControllerApi.md#delete_using_delete) | **DELETE** /pipelineTemplates/{id} | Delete a pipeline template.
[**get_using_get**](PipelineTemplatesControllerApi.md#get_using_get) | **GET** /pipelineTemplates/{id} | Get a pipeline template.
[**list_pipeline_template_dependents_using_get**](PipelineTemplatesControllerApi.md#list_pipeline_template_dependents_using_get) | **GET** /pipelineTemplates/{id}/dependents | List all pipelines that implement a pipeline template
[**list_using_get**](PipelineTemplatesControllerApi.md#list_using_get) | **GET** /pipelineTemplates | List pipeline templates.
[**resolve_templates_using_get**](PipelineTemplatesControllerApi.md#resolve_templates_using_get) | **GET** /pipelineTemplates/resolve | Resolve a pipeline template.
[**update_using_post**](PipelineTemplatesControllerApi.md#update_using_post) | **POST** /pipelineTemplates/{id} | Update a pipeline template.


# **create_using_post**
> create_using_post(pipeline_template)

Create a pipeline template.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.PipelineTemplatesControllerApi()
pipeline_template = NULL # object | pipelineTemplate

try:
    # Create a pipeline template.
    api_instance.create_using_post(pipeline_template)
except ApiException as e:
    print("Exception when calling PipelineTemplatesControllerApi->create_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_template** | **object**| pipelineTemplate | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete**
> dict(str, object) delete_using_delete(id, application=application)

Delete a pipeline template.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.PipelineTemplatesControllerApi()
id = 'id_example' # str | id
application = 'application_example' # str | application (optional)

try:
    # Delete a pipeline template.
    api_response = api_instance.delete_using_delete(id, application=application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineTemplatesControllerApi->delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **application** | **str**| application | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get**
> dict(str, object) get_using_get(id)

Get a pipeline template.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.PipelineTemplatesControllerApi()
id = 'id_example' # str | id

try:
    # Get a pipeline template.
    api_response = api_instance.get_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineTemplatesControllerApi->get_using_get: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipeline_template_dependents_using_get**
> list[object] list_pipeline_template_dependents_using_get(id, recursive=recursive)

List all pipelines that implement a pipeline template

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.PipelineTemplatesControllerApi()
id = 'id_example' # str | id
recursive = true # bool | recursive (optional)

try:
    # List all pipelines that implement a pipeline template
    api_response = api_instance.list_pipeline_template_dependents_using_get(id, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineTemplatesControllerApi->list_pipeline_template_dependents_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **recursive** | **bool**| recursive | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_using_get**
> list[object] list_using_get(scopes=scopes)

List pipeline templates.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.PipelineTemplatesControllerApi()
scopes = ['scopes_example'] # list[str] | scopes (optional)

try:
    # List pipeline templates.
    api_response = api_instance.list_using_get(scopes=scopes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineTemplatesControllerApi->list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scopes** | [**list[str]**](str.md)| scopes | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_templates_using_get**
> dict(str, object) resolve_templates_using_get(source, execution_id=execution_id, pipeline_config_id=pipeline_config_id)

Resolve a pipeline template.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.PipelineTemplatesControllerApi()
source = 'source_example' # str | source
execution_id = 'execution_id_example' # str | executionId (optional)
pipeline_config_id = 'pipeline_config_id_example' # str | pipelineConfigId (optional)

try:
    # Resolve a pipeline template.
    api_response = api_instance.resolve_templates_using_get(source, execution_id=execution_id, pipeline_config_id=pipeline_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineTemplatesControllerApi->resolve_templates_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| source | 
 **execution_id** | **str**| executionId | [optional] 
 **pipeline_config_id** | **str**| pipelineConfigId | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_post**
> update_using_post(id, pipeline_template, skip_plan_dependents=skip_plan_dependents)

Update a pipeline template.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.PipelineTemplatesControllerApi()
id = 'id_example' # str | id
pipeline_template = NULL # object | pipelineTemplate
skip_plan_dependents = false # bool | skipPlanDependents (optional) (default to false)

try:
    # Update a pipeline template.
    api_instance.update_using_post(id, pipeline_template, skip_plan_dependents=skip_plan_dependents)
except ApiException as e:
    print("Exception when calling PipelineTemplatesControllerApi->update_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **pipeline_template** | **object**| pipelineTemplate | 
 **skip_plan_dependents** | **bool**| skipPlanDependents | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

