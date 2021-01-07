# spinnaker_client.ProjectControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_pipelines_for_project_using_get**](ProjectControllerApi.md#all_pipelines_for_project_using_get) | **GET** /projects/{id}/pipelines | Get all pipelines for project
[**all_using_get3**](ProjectControllerApi.md#all_using_get3) | **GET** /projects | Get all projects
[**get_clusters_using_get3**](ProjectControllerApi.md#get_clusters_using_get3) | **GET** /projects/{id}/clusters | Get a project&#39;s clusters
[**get_using_get1**](ProjectControllerApi.md#get_using_get1) | **GET** /projects/{id} | Get a project


# **all_pipelines_for_project_using_get**
> list[object] all_pipelines_for_project_using_get(id, limit=limit, statuses=statuses)

Get all pipelines for project

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ProjectControllerApi()
id = 'id_example' # str | id
limit = 5 # int | limit (optional) (default to 5)
statuses = 'statuses_example' # str | statuses (optional)

try:
    # Get all pipelines for project
    api_response = api_instance.all_pipelines_for_project_using_get(id, limit=limit, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectControllerApi->all_pipelines_for_project_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **limit** | **int**| limit | [optional] [default to 5]
 **statuses** | **str**| statuses | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_using_get3**
> list[object] all_using_get3()

Get all projects

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ProjectControllerApi()

try:
    # Get all projects
    api_response = api_instance.all_using_get3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectControllerApi->all_using_get3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_using_get3**
> list[object] get_clusters_using_get3(id, x_rate_limit_app=x_rate_limit_app)

Get a project's clusters

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ProjectControllerApi()
id = 'id_example' # str | id
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Get a project's clusters
    api_response = api_instance.get_clusters_using_get3(id, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectControllerApi->get_clusters_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get1**
> dict(str, object) get_using_get1(id)

Get a project

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ProjectControllerApi()
id = 'id_example' # str | id

try:
    # Get a project
    api_response = api_instance.get_using_get1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectControllerApi->get_using_get1: %s\n" % e)
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

