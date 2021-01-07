# spinnaker_swagger_client.CiControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build_output_by_id_using_get**](CiControllerApi.md#get_build_output_by_id_using_get) | **GET** /ci/builds/{buildId}/output | getBuildOutputById
[**get_builds_using_get1**](CiControllerApi.md#get_builds_using_get1) | **GET** /ci/builds | getBuilds


# **get_build_output_by_id_using_get**
> object get_build_output_by_id_using_get(build_id)

getBuildOutputById

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.CiControllerApi()
build_id = 'build_id_example' # str | buildId

try:
    # getBuildOutputById
    api_response = api_instance.get_build_output_by_id_using_get(build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CiControllerApi->get_build_output_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **str**| buildId | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds_using_get1**
> list[Mapstringobject] get_builds_using_get1(build_number=build_number, commit_id=commit_id, completion_status=completion_status, project_key=project_key, repo_slug=repo_slug)

getBuilds

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.CiControllerApi()
build_number = 'build_number_example' # str | buildNumber (optional)
commit_id = 'commit_id_example' # str | commitId (optional)
completion_status = 'completion_status_example' # str | completionStatus (optional)
project_key = 'project_key_example' # str | projectKey (optional)
repo_slug = 'repo_slug_example' # str | repoSlug (optional)

try:
    # getBuilds
    api_response = api_instance.get_builds_using_get1(build_number=build_number, commit_id=commit_id, completion_status=completion_status, project_key=project_key, repo_slug=repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CiControllerApi->get_builds_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_number** | **str**| buildNumber | [optional] 
 **commit_id** | **str**| commitId | [optional] 
 **completion_status** | **str**| completionStatus | [optional] 
 **project_key** | **str**| projectKey | [optional] 
 **repo_slug** | **str**| repoSlug | [optional] 

### Return type

[**list[Mapstringobject]**](Mapstringobject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

