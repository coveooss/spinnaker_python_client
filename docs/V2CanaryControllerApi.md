# spinnaker_swagger_client.V2CanaryControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_canary_result_using_get**](V2CanaryControllerApi.md#get_canary_result_using_get) | **GET** /v2/canaries/canary/{canaryConfigId}/{canaryExecutionId} | (DEPRECATED) Retrieve a canary result
[**get_canary_result_using_get1**](V2CanaryControllerApi.md#get_canary_result_using_get1) | **GET** /v2/canaries/canary/{canaryExecutionId} | Retrieve a canary result
[**get_canary_results_by_application_using_get**](V2CanaryControllerApi.md#get_canary_results_by_application_using_get) | **GET** /v2/canaries/{application}/executions | Retrieve a list of an application&#39;s canary results
[**get_metric_set_pair_list_using_get**](V2CanaryControllerApi.md#get_metric_set_pair_list_using_get) | **GET** /v2/canaries/metricSetPairList/{metricSetPairListId} | Retrieve a metric set pair list
[**initiate_canary_using_post**](V2CanaryControllerApi.md#initiate_canary_using_post) | **POST** /v2/canaries/canary/{canaryConfigId} | Start a canary execution
[**initiate_canary_with_config_using_post**](V2CanaryControllerApi.md#initiate_canary_with_config_using_post) | **POST** /v2/canaries/canary | Start a canary execution with the supplied canary config
[**list_credentials_using_get**](V2CanaryControllerApi.md#list_credentials_using_get) | **GET** /v2/canaries/credentials | Retrieve a list of configured Kayenta accounts
[**list_judges_using_get**](V2CanaryControllerApi.md#list_judges_using_get) | **GET** /v2/canaries/judges | Retrieve a list of all configured canary judges
[**list_metrics_service_metadata_using_get**](V2CanaryControllerApi.md#list_metrics_service_metadata_using_get) | **GET** /v2/canaries/metadata/metricsService | Retrieve a list of descriptors for use in populating the canary config ui


# **get_canary_result_using_get**
> object get_canary_result_using_get(canary_config_id, canary_execution_id, storage_account_name=storage_account_name)

(DEPRECATED) Retrieve a canary result

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.V2CanaryControllerApi()
canary_config_id = 'canary_config_id_example' # str | canaryConfigId
canary_execution_id = 'canary_execution_id_example' # str | canaryExecutionId
storage_account_name = 'storage_account_name_example' # str | storageAccountName (optional)

try:
    # (DEPRECATED) Retrieve a canary result
    api_response = api_instance.get_canary_result_using_get(canary_config_id, canary_execution_id, storage_account_name=storage_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryControllerApi->get_canary_result_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canary_config_id** | **str**| canaryConfigId | 
 **canary_execution_id** | **str**| canaryExecutionId | 
 **storage_account_name** | **str**| storageAccountName | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canary_result_using_get1**
> object get_canary_result_using_get1(canary_execution_id, storage_account_name=storage_account_name)

Retrieve a canary result

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.V2CanaryControllerApi()
canary_execution_id = 'canary_execution_id_example' # str | canaryExecutionId
storage_account_name = 'storage_account_name_example' # str | storageAccountName (optional)

try:
    # Retrieve a canary result
    api_response = api_instance.get_canary_result_using_get1(canary_execution_id, storage_account_name=storage_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryControllerApi->get_canary_result_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canary_execution_id** | **str**| canaryExecutionId | 
 **storage_account_name** | **str**| storageAccountName | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canary_results_by_application_using_get**
> list[object] get_canary_results_by_application_using_get(application, limit, page=page, statuses=statuses, storage_account_name=storage_account_name)

Retrieve a list of an application's canary results

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.V2CanaryControllerApi()
application = 'application_example' # str | application
limit = 56 # int | limit
page = 1 # int | page (optional) (default to 1)
statuses = 'statuses_example' # str | Comma-separated list of statuses, e.g.: RUNNING, SUCCEEDED, TERMINAL (optional)
storage_account_name = 'storage_account_name_example' # str | storageAccountName (optional)

try:
    # Retrieve a list of an application's canary results
    api_response = api_instance.get_canary_results_by_application_using_get(application, limit, page=page, statuses=statuses, storage_account_name=storage_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryControllerApi->get_canary_results_by_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **limit** | **int**| limit | 
 **page** | **int**| page | [optional] [default to 1]
 **statuses** | **str**| Comma-separated list of statuses, e.g.: RUNNING, SUCCEEDED, TERMINAL | [optional] 
 **storage_account_name** | **str**| storageAccountName | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metric_set_pair_list_using_get**
> list[object] get_metric_set_pair_list_using_get(metric_set_pair_list_id, storage_account_name=storage_account_name)

Retrieve a metric set pair list

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.V2CanaryControllerApi()
metric_set_pair_list_id = 'metric_set_pair_list_id_example' # str | metricSetPairListId
storage_account_name = 'storage_account_name_example' # str | storageAccountName (optional)

try:
    # Retrieve a metric set pair list
    api_response = api_instance.get_metric_set_pair_list_using_get(metric_set_pair_list_id, storage_account_name=storage_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryControllerApi->get_metric_set_pair_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_set_pair_list_id** | **str**| metricSetPairListId | 
 **storage_account_name** | **str**| storageAccountName | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_canary_using_post**
> object initiate_canary_using_post(canary_config_id, execution_request, application=application, configuration_account_name=configuration_account_name, metrics_account_name=metrics_account_name, parent_pipeline_execution_id=parent_pipeline_execution_id, storage_account_name=storage_account_name)

Start a canary execution

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.V2CanaryControllerApi()
canary_config_id = 'canary_config_id_example' # str | canaryConfigId
execution_request = NULL # object | executionRequest
application = 'application_example' # str | application (optional)
configuration_account_name = 'configuration_account_name_example' # str | configurationAccountName (optional)
metrics_account_name = 'metrics_account_name_example' # str | metricsAccountName (optional)
parent_pipeline_execution_id = 'parent_pipeline_execution_id_example' # str | parentPipelineExecutionId (optional)
storage_account_name = 'storage_account_name_example' # str | storageAccountName (optional)

try:
    # Start a canary execution
    api_response = api_instance.initiate_canary_using_post(canary_config_id, execution_request, application=application, configuration_account_name=configuration_account_name, metrics_account_name=metrics_account_name, parent_pipeline_execution_id=parent_pipeline_execution_id, storage_account_name=storage_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryControllerApi->initiate_canary_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canary_config_id** | **str**| canaryConfigId | 
 **execution_request** | **object**| executionRequest | 
 **application** | **str**| application | [optional] 
 **configuration_account_name** | **str**| configurationAccountName | [optional] 
 **metrics_account_name** | **str**| metricsAccountName | [optional] 
 **parent_pipeline_execution_id** | **str**| parentPipelineExecutionId | [optional] 
 **storage_account_name** | **str**| storageAccountName | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_canary_with_config_using_post**
> object initiate_canary_with_config_using_post(adhoc_execution_request, application=application, metrics_account_name=metrics_account_name, parent_pipeline_execution_id=parent_pipeline_execution_id, storage_account_name=storage_account_name)

Start a canary execution with the supplied canary config

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.V2CanaryControllerApi()
adhoc_execution_request = NULL # object | adhocExecutionRequest
application = 'application_example' # str | application (optional)
metrics_account_name = 'metrics_account_name_example' # str | metricsAccountName (optional)
parent_pipeline_execution_id = 'parent_pipeline_execution_id_example' # str | parentPipelineExecutionId (optional)
storage_account_name = 'storage_account_name_example' # str | storageAccountName (optional)

try:
    # Start a canary execution with the supplied canary config
    api_response = api_instance.initiate_canary_with_config_using_post(adhoc_execution_request, application=application, metrics_account_name=metrics_account_name, parent_pipeline_execution_id=parent_pipeline_execution_id, storage_account_name=storage_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryControllerApi->initiate_canary_with_config_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adhoc_execution_request** | **object**| adhocExecutionRequest | 
 **application** | **str**| application | [optional] 
 **metrics_account_name** | **str**| metricsAccountName | [optional] 
 **parent_pipeline_execution_id** | **str**| parentPipelineExecutionId | [optional] 
 **storage_account_name** | **str**| storageAccountName | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credentials_using_get**
> list[object] list_credentials_using_get()

Retrieve a list of configured Kayenta accounts

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.V2CanaryControllerApi()

try:
    # Retrieve a list of configured Kayenta accounts
    api_response = api_instance.list_credentials_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryControllerApi->list_credentials_using_get: %s\n" % e)
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

# **list_judges_using_get**
> list[object] list_judges_using_get()

Retrieve a list of all configured canary judges

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.V2CanaryControllerApi()

try:
    # Retrieve a list of all configured canary judges
    api_response = api_instance.list_judges_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryControllerApi->list_judges_using_get: %s\n" % e)
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

# **list_metrics_service_metadata_using_get**
> list[object] list_metrics_service_metadata_using_get(filter=filter, metrics_account_name=metrics_account_name)

Retrieve a list of descriptors for use in populating the canary config ui

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.V2CanaryControllerApi()
filter = 'filter_example' # str | filter (optional)
metrics_account_name = 'metrics_account_name_example' # str | metricsAccountName (optional)

try:
    # Retrieve a list of descriptors for use in populating the canary config ui
    api_response = api_instance.list_metrics_service_metadata_using_get(filter=filter, metrics_account_name=metrics_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryControllerApi->list_metrics_service_metadata_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| filter | [optional] 
 **metrics_account_name** | **str**| metricsAccountName | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

