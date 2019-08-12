# swagger_client.ConcourseControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobs_using_get**](ConcourseControllerApi.md#jobs_using_get) | **GET** /concourse/{buildMaster}/teams/{team}/pipelines/{pipeline}/jobs | Retrieve the list of job names for a given pipeline available to triggers
[**pipelines_using_get**](ConcourseControllerApi.md#pipelines_using_get) | **GET** /concourse/{buildMaster}/teams/{team}/pipelines | Retrieve the list of pipeline names for a given team available to triggers
[**resources_using_get**](ConcourseControllerApi.md#resources_using_get) | **GET** /concourse/{buildMaster}/teams/{team}/pipelines/{pipeline}/resources | Retrieve the list of resource names for a given pipeline available to the Concourse stage


# **jobs_using_get**
> list[object] jobs_using_get(build_master, team, pipeline)

Retrieve the list of job names for a given pipeline available to triggers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConcourseControllerApi()
build_master = 'build_master_example' # str | buildMaster
team = 'team_example' # str | team
pipeline = 'pipeline_example' # str | pipeline

try:
    # Retrieve the list of job names for a given pipeline available to triggers
    api_response = api_instance.jobs_using_get(build_master, team, pipeline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConcourseControllerApi->jobs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 
 **team** | **str**| team | 
 **pipeline** | **str**| pipeline | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_using_get**
> list[object] pipelines_using_get(build_master, team)

Retrieve the list of pipeline names for a given team available to triggers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConcourseControllerApi()
build_master = 'build_master_example' # str | buildMaster
team = 'team_example' # str | team

try:
    # Retrieve the list of pipeline names for a given team available to triggers
    api_response = api_instance.pipelines_using_get(build_master, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConcourseControllerApi->pipelines_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 
 **team** | **str**| team | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_using_get**
> list[object] resources_using_get(build_master, team, pipeline)

Retrieve the list of resource names for a given pipeline available to the Concourse stage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConcourseControllerApi()
build_master = 'build_master_example' # str | buildMaster
team = 'team_example' # str | team
pipeline = 'pipeline_example' # str | pipeline

try:
    # Retrieve the list of resource names for a given pipeline available to the Concourse stage
    api_response = api_instance.resources_using_get(build_master, team, pipeline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConcourseControllerApi->resources_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 
 **team** | **str**| team | 
 **pipeline** | **str**| pipeline | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

