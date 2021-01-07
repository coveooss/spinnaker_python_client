# spinnaker-python-client.V2CanaryConfigControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_canary_config_using_post**](V2CanaryConfigControllerApi.md#create_canary_config_using_post) | **POST** /v2/canaryConfig | Create a canary configuration
[**delete_canary_config_using_delete**](V2CanaryConfigControllerApi.md#delete_canary_config_using_delete) | **DELETE** /v2/canaryConfig/{id} | Delete a canary configuration
[**get_canary_config_using_get**](V2CanaryConfigControllerApi.md#get_canary_config_using_get) | **GET** /v2/canaryConfig/{id} | Retrieve a canary configuration by id
[**get_canary_configs_using_get**](V2CanaryConfigControllerApi.md#get_canary_configs_using_get) | **GET** /v2/canaryConfig | Retrieve a list of canary configurations
[**update_canary_config_using_put**](V2CanaryConfigControllerApi.md#update_canary_config_using_put) | **PUT** /v2/canaryConfig/{id} | Update a canary configuration


# **create_canary_config_using_post**
> object create_canary_config_using_post(config, configuration_account_name=configuration_account_name)

Create a canary configuration

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.V2CanaryConfigControllerApi()
config = NULL # object | config
configuration_account_name = 'configuration_account_name_example' # str | configurationAccountName (optional)

try:
    # Create a canary configuration
    api_response = api_instance.create_canary_config_using_post(config, configuration_account_name=configuration_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryConfigControllerApi->create_canary_config_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **object**| config | 
 **configuration_account_name** | **str**| configurationAccountName | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_canary_config_using_delete**
> delete_canary_config_using_delete(id, configuration_account_name=configuration_account_name)

Delete a canary configuration

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.V2CanaryConfigControllerApi()
id = 'id_example' # str | id
configuration_account_name = 'configuration_account_name_example' # str | configurationAccountName (optional)

try:
    # Delete a canary configuration
    api_instance.delete_canary_config_using_delete(id, configuration_account_name=configuration_account_name)
except ApiException as e:
    print("Exception when calling V2CanaryConfigControllerApi->delete_canary_config_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **configuration_account_name** | **str**| configurationAccountName | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canary_config_using_get**
> object get_canary_config_using_get(id, configuration_account_name=configuration_account_name)

Retrieve a canary configuration by id

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.V2CanaryConfigControllerApi()
id = 'id_example' # str | id
configuration_account_name = 'configuration_account_name_example' # str | configurationAccountName (optional)

try:
    # Retrieve a canary configuration by id
    api_response = api_instance.get_canary_config_using_get(id, configuration_account_name=configuration_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryConfigControllerApi->get_canary_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **configuration_account_name** | **str**| configurationAccountName | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canary_configs_using_get**
> list[object] get_canary_configs_using_get(application=application, configuration_account_name=configuration_account_name)

Retrieve a list of canary configurations

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.V2CanaryConfigControllerApi()
application = 'application_example' # str | application (optional)
configuration_account_name = 'configuration_account_name_example' # str | configurationAccountName (optional)

try:
    # Retrieve a list of canary configurations
    api_response = api_instance.get_canary_configs_using_get(application=application, configuration_account_name=configuration_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryConfigControllerApi->get_canary_configs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | [optional] 
 **configuration_account_name** | **str**| configurationAccountName | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_canary_config_using_put**
> object update_canary_config_using_put(config, id, configuration_account_name=configuration_account_name)

Update a canary configuration

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.V2CanaryConfigControllerApi()
config = NULL # object | config
id = 'id_example' # str | id
configuration_account_name = 'configuration_account_name_example' # str | configurationAccountName (optional)

try:
    # Update a canary configuration
    api_response = api_instance.update_canary_config_using_put(config, id, configuration_account_name=configuration_account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2CanaryConfigControllerApi->update_canary_config_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **object**| config | 
 **id** | **str**| id | 
 **configuration_account_name** | **str**| configurationAccountName | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

