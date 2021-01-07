# spinnaker_client.ApplicationControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_pipeline_using_put**](ApplicationControllerApi.md#cancel_pipeline_using_put) | **PUT** /applications/{application}/pipelines/{id}/cancel | Cancel pipeline
[**cancel_task_using_put**](ApplicationControllerApi.md#cancel_task_using_put) | **PUT** /applications/{application}/tasks/{id}/cancel | Cancel task
[**get_all_applications_using_get**](ApplicationControllerApi.md#get_all_applications_using_get) | **GET** /applications | Retrieve a list of applications
[**get_application_history_using_get**](ApplicationControllerApi.md#get_application_history_using_get) | **GET** /applications/{application}/history | Retrieve a list of an application&#39;s configuration revision history
[**get_application_using_get**](ApplicationControllerApi.md#get_application_using_get) | **GET** /applications/{application} | Retrieve an application&#39;s details
[**get_pipeline_config_using_get**](ApplicationControllerApi.md#get_pipeline_config_using_get) | **GET** /applications/{application}/pipelineConfigs/{pipelineName} | Retrieve a pipeline configuration
[**get_pipeline_configs_for_application_using_get**](ApplicationControllerApi.md#get_pipeline_configs_for_application_using_get) | **GET** /applications/{application}/pipelineConfigs | Retrieve a list of an application&#39;s pipeline configurations
[**get_pipelines_using_get**](ApplicationControllerApi.md#get_pipelines_using_get) | **GET** /applications/{application}/pipelines | Retrieve a list of an application&#39;s pipeline executions
[**get_strategy_config_using_get**](ApplicationControllerApi.md#get_strategy_config_using_get) | **GET** /applications/{application}/strategyConfigs/{strategyName} | Retrieve a pipeline strategy configuration
[**get_strategy_configs_for_application_using_get**](ApplicationControllerApi.md#get_strategy_configs_for_application_using_get) | **GET** /applications/{application}/strategyConfigs | Retrieve a list of an application&#39;s pipeline strategy configurations
[**get_task_details_using_get**](ApplicationControllerApi.md#get_task_details_using_get) | **GET** /applications/{application}/tasks/{id}/details/{taskDetailsId} | Get task details
[**get_task_using_get**](ApplicationControllerApi.md#get_task_using_get) | **GET** /applications/{application}/tasks/{id} | Get task
[**get_tasks_using_get**](ApplicationControllerApi.md#get_tasks_using_get) | **GET** /applications/{application}/tasks | Retrieve a list of an application&#39;s tasks
[**invoke_pipeline_config_using_post**](ApplicationControllerApi.md#invoke_pipeline_config_using_post) | **POST** /applications/{application}/pipelineConfigs/{pipelineName} | Invoke pipeline config
[**task_using_post**](ApplicationControllerApi.md#task_using_post) | **POST** /applications/{application}/tasks | Create task


# **cancel_pipeline_using_put**
> dict(str, object) cancel_pipeline_using_put(id, reason=reason)

Cancel pipeline

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
id = 'id_example' # str | id
reason = 'reason_example' # str | reason (optional)

try:
    # Cancel pipeline
    api_response = api_instance.cancel_pipeline_using_put(id, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->cancel_pipeline_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **reason** | **str**| reason | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_task_using_put**
> dict(str, object) cancel_task_using_put(id)

Cancel task

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
id = 'id_example' # str | id

try:
    # Cancel task
    api_response = api_instance.cancel_task_using_put(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->cancel_task_using_put: %s\n" % e)
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

# **get_all_applications_using_get**
> list[object] get_all_applications_using_get(account=account, owner=owner)

Retrieve a list of applications

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
account = 'account_example' # str | filters results to only include applications deployed in the specified account (optional)
owner = 'owner_example' # str | filters results to only include applications owned by the specified email (optional)

try:
    # Retrieve a list of applications
    api_response = api_instance.get_all_applications_using_get(account=account, owner=owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_all_applications_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| filters results to only include applications deployed in the specified account | [optional] 
 **owner** | **str**| filters results to only include applications owned by the specified email | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_history_using_get**
> list[object] get_application_history_using_get(application, limit=limit)

Retrieve a list of an application's configuration revision history

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application
limit = 20 # int | limit (optional) (default to 20)

try:
    # Retrieve a list of an application's configuration revision history
    api_response = api_instance.get_application_history_using_get(application, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_application_using_get**
> dict(str, object) get_application_using_get(application, expand=expand)

Retrieve an application's details

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application
expand = true # bool | expand (optional) (default to true)

try:
    # Retrieve an application's details
    api_response = api_instance.get_application_using_get(application, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **expand** | **bool**| expand | [optional] [default to true]

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_config_using_get**
> dict(str, object) get_pipeline_config_using_get(application, pipeline_name)

Retrieve a pipeline configuration

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application
pipeline_name = 'pipeline_name_example' # str | pipelineName

try:
    # Retrieve a pipeline configuration
    api_response = api_instance.get_pipeline_config_using_get(application, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_pipeline_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **pipeline_name** | **str**| pipelineName | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_configs_for_application_using_get**
> list[object] get_pipeline_configs_for_application_using_get(application)

Retrieve a list of an application's pipeline configurations

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application

try:
    # Retrieve a list of an application's pipeline configurations
    api_response = api_instance.get_pipeline_configs_for_application_using_get(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_pipeline_configs_for_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipelines_using_get**
> list[object] get_pipelines_using_get(application, expand=expand, limit=limit, statuses=statuses)

Retrieve a list of an application's pipeline executions

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application
expand = true # bool | expand (optional)
limit = 56 # int | limit (optional)
statuses = 'statuses_example' # str | statuses (optional)

try:
    # Retrieve a list of an application's pipeline executions
    api_response = api_instance.get_pipelines_using_get(application, expand=expand, limit=limit, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_pipelines_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **expand** | **bool**| expand | [optional] 
 **limit** | **int**| limit | [optional] 
 **statuses** | **str**| statuses | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_strategy_config_using_get**
> dict(str, object) get_strategy_config_using_get(application, strategy_name)

Retrieve a pipeline strategy configuration

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application
strategy_name = 'strategy_name_example' # str | strategyName

try:
    # Retrieve a pipeline strategy configuration
    api_response = api_instance.get_strategy_config_using_get(application, strategy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_strategy_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **strategy_name** | **str**| strategyName | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_strategy_configs_for_application_using_get**
> list[object] get_strategy_configs_for_application_using_get(application)

Retrieve a list of an application's pipeline strategy configurations

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application

try:
    # Retrieve a list of an application's pipeline strategy configurations
    api_response = api_instance.get_strategy_configs_for_application_using_get(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_strategy_configs_for_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_details_using_get**
> dict(str, object) get_task_details_using_get(id, task_details_id, x_rate_limit_app=x_rate_limit_app)

Get task details

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
id = 'id_example' # str | id
task_details_id = 'task_details_id_example' # str | taskDetailsId
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Get task details
    api_response = api_instance.get_task_details_using_get(id, task_details_id, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_task_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **task_details_id** | **str**| taskDetailsId | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_using_get**
> dict(str, object) get_task_using_get(id)

Get task

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
id = 'id_example' # str | id

try:
    # Get task
    api_response = api_instance.get_task_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_task_using_get: %s\n" % e)
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

# **get_tasks_using_get**
> list[object] get_tasks_using_get(application, limit=limit, page=page, statuses=statuses)

Retrieve a list of an application's tasks

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application
limit = 56 # int | limit (optional)
page = 56 # int | page (optional)
statuses = 'statuses_example' # str | statuses (optional)

try:
    # Retrieve a list of an application's tasks
    api_response = api_instance.get_tasks_using_get(application, limit=limit, page=page, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_tasks_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **limit** | **int**| limit | [optional] 
 **page** | **int**| page | [optional] 
 **statuses** | **str**| statuses | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_pipeline_config_using_post**
> HttpEntity invoke_pipeline_config_using_post(application, pipeline_name, trigger=trigger, user=user)

Invoke pipeline config

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application
pipeline_name = 'pipeline_name_example' # str | pipelineName
trigger = NULL # object | trigger (optional)
user = 'user_example' # str | user (optional)

try:
    # Invoke pipeline config
    api_response = api_instance.invoke_pipeline_config_using_post(application, pipeline_name, trigger=trigger, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->invoke_pipeline_config_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **pipeline_name** | **str**| pipelineName | 
 **trigger** | **object**| trigger | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**HttpEntity**](HttpEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_using_post**
> dict(str, object) task_using_post(application, map)

Create task

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ApplicationControllerApi()
application = 'application_example' # str | application
map = NULL # object | map

try:
    # Create task
    api_response = api_instance.task_using_post(application, map)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->task_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **map** | **object**| map | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

