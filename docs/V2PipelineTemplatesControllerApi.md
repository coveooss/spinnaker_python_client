# swagger_client.V2PipelineTemplatesControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post1**](V2PipelineTemplatesControllerApi.md#create_using_post1) | **POST** /v2/pipelineTemplates/create | (ALPHA) Create a pipeline template.
[**delete_using_delete1**](V2PipelineTemplatesControllerApi.md#delete_using_delete1) | **DELETE** /v2/pipelineTemplates/{id} | Delete a pipeline template.
[**get_using_get2**](V2PipelineTemplatesControllerApi.md#get_using_get2) | **GET** /v2/pipelineTemplates/{id} | (ALPHA) Get a pipeline template.
[**list_pipeline_template_dependents_using_get1**](V2PipelineTemplatesControllerApi.md#list_pipeline_template_dependents_using_get1) | **GET** /v2/pipelineTemplates/{id}/dependents | (ALPHA) List all pipelines that implement a pipeline template
[**list_using_get1**](V2PipelineTemplatesControllerApi.md#list_using_get1) | **GET** /v2/pipelineTemplates | (ALPHA) List pipeline templates.
[**plan_using_post**](V2PipelineTemplatesControllerApi.md#plan_using_post) | **POST** /v2/pipelineTemplates/plan | (ALPHA) Plan a pipeline template configuration.
[**update_using_post1**](V2PipelineTemplatesControllerApi.md#update_using_post1) | **POST** /v2/pipelineTemplates/update/{id} | (ALPHA) Update a pipeline template.


# **create_using_post1**
> create_using_post1(pipeline_template, tag=tag)

(ALPHA) Create a pipeline template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.V2PipelineTemplatesControllerApi()
pipeline_template = NULL # object | pipelineTemplate
tag = 'tag_example' # str | tag (optional)

try:
    # (ALPHA) Create a pipeline template.
    api_instance.create_using_post1(pipeline_template, tag=tag)
except ApiException as e:
    print("Exception when calling V2PipelineTemplatesControllerApi->create_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_template** | **object**| pipelineTemplate | 
 **tag** | **str**| tag | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete1**
> dict(str, object) delete_using_delete1(id, tag=tag, digest=digest, application=application)

Delete a pipeline template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.V2PipelineTemplatesControllerApi()
id = 'id_example' # str | id
tag = 'tag_example' # str | tag (optional)
digest = 'digest_example' # str | digest (optional)
application = 'application_example' # str | application (optional)

try:
    # Delete a pipeline template.
    api_response = api_instance.delete_using_delete1(id, tag=tag, digest=digest, application=application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2PipelineTemplatesControllerApi->delete_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **tag** | **str**| tag | [optional] 
 **digest** | **str**| digest | [optional] 
 **application** | **str**| application | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get2**
> dict(str, object) get_using_get2(id, tag=tag, digest=digest)

(ALPHA) Get a pipeline template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.V2PipelineTemplatesControllerApi()
id = 'id_example' # str | id
tag = 'tag_example' # str | tag (optional)
digest = 'digest_example' # str | digest (optional)

try:
    # (ALPHA) Get a pipeline template.
    api_response = api_instance.get_using_get2(id, tag=tag, digest=digest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2PipelineTemplatesControllerApi->get_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **tag** | **str**| tag | [optional] 
 **digest** | **str**| digest | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipeline_template_dependents_using_get1**
> list[object] list_pipeline_template_dependents_using_get1(id)

(ALPHA) List all pipelines that implement a pipeline template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.V2PipelineTemplatesControllerApi()
id = 'id_example' # str | id

try:
    # (ALPHA) List all pipelines that implement a pipeline template
    api_response = api_instance.list_pipeline_template_dependents_using_get1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2PipelineTemplatesControllerApi->list_pipeline_template_dependents_using_get1: %s\n" % e)
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

# **list_using_get1**
> list[object] list_using_get1(scopes=scopes)

(ALPHA) List pipeline templates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.V2PipelineTemplatesControllerApi()
scopes = ['scopes_example'] # list[str] | scopes (optional)

try:
    # (ALPHA) List pipeline templates.
    api_response = api_instance.list_using_get1(scopes=scopes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2PipelineTemplatesControllerApi->list_using_get1: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_using_post**
> dict(str, object) plan_using_post(pipeline)

(ALPHA) Plan a pipeline template configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.V2PipelineTemplatesControllerApi()
pipeline = NULL # object | pipeline

try:
    # (ALPHA) Plan a pipeline template configuration.
    api_response = api_instance.plan_using_post(pipeline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2PipelineTemplatesControllerApi->plan_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | **object**| pipeline | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_post1**
> update_using_post1(id, pipeline_template, tag=tag, skip_plan_dependents=skip_plan_dependents)

(ALPHA) Update a pipeline template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.V2PipelineTemplatesControllerApi()
id = 'id_example' # str | id
pipeline_template = NULL # object | pipelineTemplate
tag = 'tag_example' # str | tag (optional)
skip_plan_dependents = false # bool | skipPlanDependents (optional) (default to false)

try:
    # (ALPHA) Update a pipeline template.
    api_instance.update_using_post1(id, pipeline_template, tag=tag, skip_plan_dependents=skip_plan_dependents)
except ApiException as e:
    print("Exception when calling V2PipelineTemplatesControllerApi->update_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **pipeline_template** | **object**| pipelineTemplate | 
 **tag** | **str**| tag | [optional] 
 **skip_plan_dependents** | **bool**| skipPlanDependents | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

