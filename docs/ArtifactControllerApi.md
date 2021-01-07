# spinnaker-python-client.ArtifactControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_using_get**](ArtifactControllerApi.md#all_using_get) | **GET** /artifacts/credentials | Retrieve the list of artifact accounts configured in Clouddriver.
[**artifact_versions_using_get**](ArtifactControllerApi.md#artifact_versions_using_get) | **GET** /artifacts/account/{accountName}/versions | Retrieve the list of artifact versions by account and artifact names
[**get_artifact_using_get**](ArtifactControllerApi.md#get_artifact_using_get) | **GET** /artifacts/{provider}/{packageName}/{version} | Retrieve the specified artifact version for an artifact provider and package name


# **all_using_get**
> list[object] all_using_get(x_rate_limit_app=x_rate_limit_app)

Retrieve the list of artifact accounts configured in Clouddriver.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.ArtifactControllerApi()
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

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifact_versions_using_get**
> list[str] artifact_versions_using_get(account_name, artifact_name, type, x_rate_limit_app=x_rate_limit_app)

Retrieve the list of artifact versions by account and artifact names

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.ArtifactControllerApi()
account_name = 'account_name_example' # str | accountName
artifact_name = 'artifact_name_example' # str | artifactName
type = 'type_example' # str | type
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve the list of artifact versions by account and artifact names
    api_response = api_instance.artifact_versions_using_get(account_name, artifact_name, type, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactControllerApi->artifact_versions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| accountName | 
 **artifact_name** | **str**| artifactName | 
 **type** | **str**| type | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_using_get**
> object get_artifact_using_get(package_name, provider, version)

Retrieve the specified artifact version for an artifact provider and package name

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.ArtifactControllerApi()
package_name = 'package_name_example' # str | packageName
provider = 'provider_example' # str | provider
version = 'version_example' # str | version

try:
    # Retrieve the specified artifact version for an artifact provider and package name
    api_response = api_instance.get_artifact_using_get(package_name, provider, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactControllerApi->get_artifact_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_name** | **str**| packageName | 
 **provider** | **str**| provider | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

