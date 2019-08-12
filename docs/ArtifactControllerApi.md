# swagger_client.ArtifactControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_using_get**](ArtifactControllerApi.md#all_using_get) | **GET** /artifacts/credentials | Retrieve the list of artifact accounts configured in Clouddriver.
[**artifact_versions_using_get**](ArtifactControllerApi.md#artifact_versions_using_get) | **GET** /artifacts/account/{accountName}/versions | Retrieve the list of artifact versions by account and artifact names


# **all_using_get**
> list[object] all_using_get(x_rate_limit_app=x_rate_limit_app)

Retrieve the list of artifact accounts configured in Clouddriver.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArtifactControllerApi()
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve the list of artifact accounts configured in Clouddriver.
    api_response = api_instance.all_using_get(x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactControllerApi->all_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifact_versions_using_get**
> list[str] artifact_versions_using_get(account_name, type, artifact_name, x_rate_limit_app=x_rate_limit_app)

Retrieve the list of artifact versions by account and artifact names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArtifactControllerApi()
account_name = 'account_name_example' # str | accountName
type = 'type_example' # str | type
artifact_name = 'artifact_name_example' # str | artifactName
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve the list of artifact versions by account and artifact names
    api_response = api_instance.artifact_versions_using_get(account_name, type, artifact_name, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactControllerApi->artifact_versions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| accountName | 
 **type** | **str**| type | 
 **artifact_name** | **str**| artifactName | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

