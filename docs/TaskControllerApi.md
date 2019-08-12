# swagger_client.TaskControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_task_using_put1**](TaskControllerApi.md#cancel_task_using_put1) | **PUT** /tasks/{id}/cancel | Cancel task
[**cancel_tasks_using_put**](TaskControllerApi.md#cancel_tasks_using_put) | **PUT** /tasks/cancel | Cancel tasks
[**delete_task_using_delete**](TaskControllerApi.md#delete_task_using_delete) | **DELETE** /tasks/{id} | Delete task
[**get_task_details_using_get1**](TaskControllerApi.md#get_task_details_using_get1) | **GET** /tasks/{id}/details/{taskDetailsId} | Get task details
[**get_task_using_get1**](TaskControllerApi.md#get_task_using_get1) | **GET** /tasks/{id} | Get task
[**task_using_post1**](TaskControllerApi.md#task_using_post1) | **POST** /tasks | Create task


# **cancel_task_using_put1**
> dict(str, object) cancel_task_using_put1(id)

Cancel task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaskControllerApi()
id = 'id_example' # str | id

try:
    # Cancel task
    api_response = api_instance.cancel_task_using_put1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskControllerApi->cancel_task_using_put1: %s\n" % e)
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

# **cancel_tasks_using_put**
> dict(str, object) cancel_tasks_using_put(ids)

Cancel tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaskControllerApi()
ids = ['ids_example'] # list[str] | ids

try:
    # Cancel tasks
    api_response = api_instance.cancel_tasks_using_put(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskControllerApi->cancel_tasks_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| ids | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task_using_delete**
> dict(str, object) delete_task_using_delete(id)

Delete task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaskControllerApi()
id = 'id_example' # str | id

try:
    # Delete task
    api_response = api_instance.delete_task_using_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskControllerApi->delete_task_using_delete: %s\n" % e)
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

# **get_task_details_using_get1**
> dict(str, object) get_task_details_using_get1(id, task_details_id, x_rate_limit_app=x_rate_limit_app)

Get task details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaskControllerApi()
id = 'id_example' # str | id
task_details_id = 'task_details_id_example' # str | taskDetailsId
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Get task details
    api_response = api_instance.get_task_details_using_get1(id, task_details_id, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskControllerApi->get_task_details_using_get1: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_using_get1**
> dict(str, object) get_task_using_get1(id)

Get task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaskControllerApi()
id = 'id_example' # str | id

try:
    # Get task
    api_response = api_instance.get_task_using_get1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskControllerApi->get_task_using_get1: %s\n" % e)
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

# **task_using_post1**
> dict(str, object) task_using_post1(map)

Create task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaskControllerApi()
map = NULL # object | map

try:
    # Create task
    api_response = api_instance.task_using_post1(map)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskControllerApi->task_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map** | **object**| map | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

