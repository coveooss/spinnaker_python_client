# spinnaker_client.ManagedControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pin_using_post**](ManagedControllerApi.md#create_pin_using_post) | **POST** /managed/application/{application}/pin | Create a pin for an artifact in an environment
[**delete_manifest_by_app_using_delete**](ManagedControllerApi.md#delete_manifest_by_app_using_delete) | **DELETE** /managed/application/{application}/config | Delete a delivery config manifest for an application
[**delete_manifest_using_delete**](ManagedControllerApi.md#delete_manifest_using_delete) | **DELETE** /managed/delivery-configs/{name} | Delete a delivery config manifest
[**delete_pin_using_delete**](ManagedControllerApi.md#delete_pin_using_delete) | **DELETE** /managed/application/{application}/pin/{targetEnvironment} | Unpin one or more artifact(s) in an environment. If the &#x60;reference&#x60; parameter is specified, only the corresponding artifact will be unpinned. If it&#39;s omitted, all pinned artifacts in the environment will be unpinned.
[**delete_veto_using_delete**](ManagedControllerApi.md#delete_veto_using_delete) | **DELETE** /managed/application/{application}/veto/{targetEnvironment}/{reference}/{version} | Remove veto of an artifact version in an environment
[**diff_manifest_using_post**](ManagedControllerApi.md#diff_manifest_using_post) | **POST** /managed/delivery-configs/diff | Ad-hoc validate and diff a config manifest
[**diff_resource_using_post**](ManagedControllerApi.md#diff_resource_using_post) | **POST** /managed/resources/diff | Ad-hoc validate and diff a resource
[**export_resource_using_get**](ManagedControllerApi.md#export_resource_using_get) | **GET** /managed/resources/export/artifact/{cloudProvider}/{account}/{clusterName} | Generates an artifact definition based on the artifact used in a running cluster
[**export_resource_using_get1**](ManagedControllerApi.md#export_resource_using_get1) | **GET** /managed/resources/export/{cloudProvider}/{account}/{type}/{name} | Generate a keel resource definition for a deployed cloud resource
[**get_application_details_using_get**](ManagedControllerApi.md#get_application_details_using_get) | **GET** /managed/application/{application} | Get managed details about an application
[**get_config_by_using_get**](ManagedControllerApi.md#get_config_by_using_get) | **GET** /managed/application/{application}/config | Get the delivery config associated with an application
[**get_constraint_state_using_get**](ManagedControllerApi.md#get_constraint_state_using_get) | **GET** /managed/application/{application}/environment/{environment}/constraints | List up-to {limit} current constraint states for an environment
[**get_manifest_artifacts_using_get**](ManagedControllerApi.md#get_manifest_artifacts_using_get) | **GET** /managed/delivery-configs/{name}/artifacts | Get the status of each version of each artifact in each environment
[**get_manifest_using_get**](ManagedControllerApi.md#get_manifest_using_get) | **GET** /managed/delivery-configs/{name} | Get a delivery config manifest
[**get_manifest_yaml_using_get**](ManagedControllerApi.md#get_manifest_yaml_using_get) | **GET** /managed/delivery-configs/{name}.yml | Get a delivery config manifest
[**get_resource_status_using_get**](ManagedControllerApi.md#get_resource_status_using_get) | **GET** /managed/resources/{resourceId}/status | Get status of a resource
[**get_resource_using_get**](ManagedControllerApi.md#get_resource_using_get) | **GET** /managed/resources/{resourceId} | Get a resource
[**get_resource_yaml_using_get**](ManagedControllerApi.md#get_resource_yaml_using_get) | **GET** /managed/resources/{resourceId}.yml | Get a resource
[**pause_application_using_post**](ManagedControllerApi.md#pause_application_using_post) | **POST** /managed/application/{application}/pause | Pause management of an entire application
[**pause_resource_using_post**](ManagedControllerApi.md#pause_resource_using_post) | **POST** /managed/resources/{resourceId}/pause | Pause management of a resource
[**resume_application_using_delete**](ManagedControllerApi.md#resume_application_using_delete) | **DELETE** /managed/application/{application}/pause | Resume management of an entire application
[**resume_resource_using_delete**](ManagedControllerApi.md#resume_resource_using_delete) | **DELETE** /managed/resources/{resourceId}/pause | Resume management of a resource
[**schema_using_get**](ManagedControllerApi.md#schema_using_get) | **GET** /managed/delivery-configs/schema | Ad-hoc validate and diff a config manifest
[**update_constraint_status_using_post**](ManagedControllerApi.md#update_constraint_status_using_post) | **POST** /managed/application/{application}/environment/{environment}/constraint | Update the status of an environment constraint
[**upsert_manifest_using_post**](ManagedControllerApi.md#upsert_manifest_using_post) | **POST** /managed/delivery-configs | Create or update a delivery config manifest
[**validate_manifest_using_post**](ManagedControllerApi.md#validate_manifest_using_post) | **POST** /managed/delivery-configs/validate | Validate a delivery config manifest
[**veto_using_post**](ManagedControllerApi.md#veto_using_post) | **POST** /managed/application/{application}/veto | Veto an artifact version in an environment


# **create_pin_using_post**
> create_pin_using_post(application, pin)

Create a pin for an artifact in an environment

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application
pin = spinnaker_client.EnvironmentArtifactPin() # EnvironmentArtifactPin | pin

try:
    # Create a pin for an artifact in an environment
    api_instance.create_pin_using_post(application, pin)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->create_pin_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **pin** | [**EnvironmentArtifactPin**](EnvironmentArtifactPin.md)| pin | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manifest_by_app_using_delete**
> DeliveryConfig delete_manifest_by_app_using_delete(application)

Delete a delivery config manifest for an application

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application

try:
    # Delete a delivery config manifest for an application
    api_response = api_instance.delete_manifest_by_app_using_delete(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->delete_manifest_by_app_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 

### Return type

[**DeliveryConfig**](DeliveryConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manifest_using_delete**
> DeliveryConfig delete_manifest_using_delete(name)

Delete a delivery config manifest

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
name = 'name_example' # str | name

try:
    # Delete a delivery config manifest
    api_response = api_instance.delete_manifest_using_delete(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->delete_manifest_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

[**DeliveryConfig**](DeliveryConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pin_using_delete**
> delete_pin_using_delete(application, target_environment, reference=reference)

Unpin one or more artifact(s) in an environment. If the `reference` parameter is specified, only the corresponding artifact will be unpinned. If it's omitted, all pinned artifacts in the environment will be unpinned.

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application
target_environment = 'target_environment_example' # str | targetEnvironment
reference = 'reference_example' # str | reference (optional)

try:
    # Unpin one or more artifact(s) in an environment. If the `reference` parameter is specified, only the corresponding artifact will be unpinned. If it's omitted, all pinned artifacts in the environment will be unpinned.
    api_instance.delete_pin_using_delete(application, target_environment, reference=reference)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->delete_pin_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **target_environment** | **str**| targetEnvironment | 
 **reference** | **str**| reference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_veto_using_delete**
> delete_veto_using_delete(application, reference, target_environment, version)

Remove veto of an artifact version in an environment

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application
reference = 'reference_example' # str | reference
target_environment = 'target_environment_example' # str | targetEnvironment
version = 'version_example' # str | version

try:
    # Remove veto of an artifact version in an environment
    api_instance.delete_veto_using_delete(application, reference, target_environment, version)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->delete_veto_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **reference** | **str**| reference | 
 **target_environment** | **str**| targetEnvironment | 
 **version** | **str**| version | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diff_manifest_using_post**
> object diff_manifest_using_post(manifest)

Ad-hoc validate and diff a config manifest

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
manifest = spinnaker_client.DeliveryConfig() # DeliveryConfig | manifest

try:
    # Ad-hoc validate and diff a config manifest
    api_response = api_instance.diff_manifest_using_post(manifest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->diff_manifest_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest** | [**DeliveryConfig**](DeliveryConfig.md)| manifest | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diff_resource_using_post**
> object diff_resource_using_post(resource)

Ad-hoc validate and diff a resource

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
resource = spinnaker_client.Resource() # Resource | resource

try:
    # Ad-hoc validate and diff a resource
    api_response = api_instance.diff_resource_using_post(resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->diff_resource_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](Resource.md)| resource | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_resource_using_get**
> object export_resource_using_get(account, cloud_provider, cluster_name)

Generates an artifact definition based on the artifact used in a running cluster

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
account = 'account_example' # str | account
cloud_provider = 'cloud_provider_example' # str | cloudProvider
cluster_name = 'cluster_name_example' # str | clusterName

try:
    # Generates an artifact definition based on the artifact used in a running cluster
    api_response = api_instance.export_resource_using_get(account, cloud_provider, cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->export_resource_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **cloud_provider** | **str**| cloudProvider | 
 **cluster_name** | **str**| clusterName | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_resource_using_get1**
> Resource export_resource_using_get1(account, cloud_provider, name, service_account, type)

Generate a keel resource definition for a deployed cloud resource

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
account = 'account_example' # str | account
cloud_provider = 'cloud_provider_example' # str | cloudProvider
name = 'name_example' # str | name
service_account = 'service_account_example' # str | serviceAccount
type = 'type_example' # str | type

try:
    # Generate a keel resource definition for a deployed cloud resource
    api_response = api_instance.export_resource_using_get1(account, cloud_provider, name, service_account, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->export_resource_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **cloud_provider** | **str**| cloudProvider | 
 **name** | **str**| name | 
 **service_account** | **str**| serviceAccount | 
 **type** | **str**| type | 

### Return type

[**Resource**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_details_using_get**
> object get_application_details_using_get(application, entities=entities, include_details=include_details, max_artifact_versions=max_artifact_versions)

Get managed details about an application

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application
entities = ['entities_example'] # list[str] | entities (optional)
include_details = false # bool | includeDetails (optional) (default to false)
max_artifact_versions = 56 # int | maxArtifactVersions (optional)

try:
    # Get managed details about an application
    api_response = api_instance.get_application_details_using_get(application, entities=entities, include_details=include_details, max_artifact_versions=max_artifact_versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->get_application_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **entities** | [**list[str]**](str.md)| entities | [optional] 
 **include_details** | **bool**| includeDetails | [optional] [default to false]
 **max_artifact_versions** | **int**| maxArtifactVersions | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_by_using_get**
> DeliveryConfig get_config_by_using_get(application)

Get the delivery config associated with an application

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application

try:
    # Get the delivery config associated with an application
    api_response = api_instance.get_config_by_using_get(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->get_config_by_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 

### Return type

[**DeliveryConfig**](DeliveryConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constraint_state_using_get**
> ConstraintState get_constraint_state_using_get(application, environment, limit=limit)

List up-to {limit} current constraint states for an environment

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application
environment = 'environment_example' # str | environment
limit = '10' # str | limit (optional) (default to 10)

try:
    # List up-to {limit} current constraint states for an environment
    api_response = api_instance.get_constraint_state_using_get(application, environment, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->get_constraint_state_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **environment** | **str**| environment | 
 **limit** | **str**| limit | [optional] [default to 10]

### Return type

[**ConstraintState**](ConstraintState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest_artifacts_using_get**
> list[object] get_manifest_artifacts_using_get(name)

Get the status of each version of each artifact in each environment

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
name = 'name_example' # str | name

try:
    # Get the status of each version of each artifact in each environment
    api_response = api_instance.get_manifest_artifacts_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->get_manifest_artifacts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest_using_get**
> DeliveryConfig get_manifest_using_get(name)

Get a delivery config manifest

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
name = 'name_example' # str | name

try:
    # Get a delivery config manifest
    api_response = api_instance.get_manifest_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->get_manifest_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

[**DeliveryConfig**](DeliveryConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest_yaml_using_get**
> DeliveryConfig get_manifest_yaml_using_get(name)

Get a delivery config manifest

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
name = 'name_example' # str | name

try:
    # Get a delivery config manifest
    api_response = api_instance.get_manifest_yaml_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->get_manifest_yaml_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

[**DeliveryConfig**](DeliveryConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_status_using_get**
> object get_resource_status_using_get(resource_id)

Get status of a resource

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
resource_id = 'resource_id_example' # str | resourceId

try:
    # Get status of a resource
    api_response = api_instance.get_resource_status_using_get(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->get_resource_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| resourceId | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_using_get**
> Resource get_resource_using_get(resource_id)

Get a resource

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
resource_id = 'resource_id_example' # str | resourceId

try:
    # Get a resource
    api_response = api_instance.get_resource_using_get(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->get_resource_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| resourceId | 

### Return type

[**Resource**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_yaml_using_get**
> Resource get_resource_yaml_using_get(resource_id)

Get a resource

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
resource_id = 'resource_id_example' # str | resourceId

try:
    # Get a resource
    api_response = api_instance.get_resource_yaml_using_get(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->get_resource_yaml_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| resourceId | 

### Return type

[**Resource**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_application_using_post**
> pause_application_using_post(application)

Pause management of an entire application

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application

try:
    # Pause management of an entire application
    api_instance.pause_application_using_post(application)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->pause_application_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_resource_using_post**
> pause_resource_using_post(resource_id)

Pause management of a resource

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
resource_id = 'resource_id_example' # str | resourceId

try:
    # Pause management of a resource
    api_instance.pause_resource_using_post(resource_id)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->pause_resource_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| resourceId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_application_using_delete**
> resume_application_using_delete(application)

Resume management of an entire application

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application

try:
    # Resume management of an entire application
    api_instance.resume_application_using_delete(application)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->resume_application_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_resource_using_delete**
> resume_resource_using_delete(resource_id)

Resume management of a resource

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
resource_id = 'resource_id_example' # str | resourceId

try:
    # Resume management of a resource
    api_instance.resume_resource_using_delete(resource_id)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->resume_resource_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| resourceId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema_using_get**
> object schema_using_get()

Ad-hoc validate and diff a config manifest

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()

try:
    # Ad-hoc validate and diff a config manifest
    api_response = api_instance.schema_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->schema_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_constraint_status_using_post**
> update_constraint_status_using_post(application, environment, status)

Update the status of an environment constraint

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application
environment = 'environment_example' # str | environment
status = spinnaker_client.ConstraintStatus() # ConstraintStatus | status

try:
    # Update the status of an environment constraint
    api_instance.update_constraint_status_using_post(application, environment, status)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->update_constraint_status_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **environment** | **str**| environment | 
 **status** | [**ConstraintStatus**](ConstraintStatus.md)| status | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_manifest_using_post**
> DeliveryConfig upsert_manifest_using_post(manifest)

Create or update a delivery config manifest

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
manifest = spinnaker_client.DeliveryConfig() # DeliveryConfig | manifest

try:
    # Create or update a delivery config manifest
    api_response = api_instance.upsert_manifest_using_post(manifest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->upsert_manifest_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest** | [**DeliveryConfig**](DeliveryConfig.md)| manifest | 

### Return type

[**DeliveryConfig**](DeliveryConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_manifest_using_post**
> object validate_manifest_using_post(manifest)

Validate a delivery config manifest

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
manifest = spinnaker_client.DeliveryConfig() # DeliveryConfig | manifest

try:
    # Validate a delivery config manifest
    api_response = api_instance.validate_manifest_using_post(manifest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->validate_manifest_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest** | [**DeliveryConfig**](DeliveryConfig.md)| manifest | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **veto_using_post**
> veto_using_post(application, veto)

Veto an artifact version in an environment

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ManagedControllerApi()
application = 'application_example' # str | application
veto = spinnaker_client.EnvironmentArtifactVeto() # EnvironmentArtifactVeto | veto

try:
    # Veto an artifact version in an environment
    api_instance.veto_using_post(application, veto)
except ApiException as e:
    print("Exception when calling ManagedControllerApi->veto_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **veto** | [**EnvironmentArtifactVeto**](EnvironmentArtifactVeto.md)| veto | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

