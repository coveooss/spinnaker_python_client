# spinnaker_swagger_client.AuthControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_accounts_using_get**](AuthControllerApi.md#get_service_accounts_using_get) | **GET** /auth/user/serviceAccounts | Get service accounts
[**logged_out_using_get**](AuthControllerApi.md#logged_out_using_get) | **GET** /auth/loggedOut | Get logged out message
[**redirect_using_get**](AuthControllerApi.md#redirect_using_get) | **GET** /auth/redirect | Redirect to Deck
[**sync_using_post**](AuthControllerApi.md#sync_using_post) | **POST** /auth/roles/sync | Sync user roles
[**user_using_get**](AuthControllerApi.md#user_using_get) | **GET** /auth/user | Get user


# **get_service_accounts_using_get**
> list[object] get_service_accounts_using_get(application=application)

Get service accounts

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.AuthControllerApi()
application = 'application_example' # str | application (optional)

try:
    # Get service accounts
    api_response = api_instance.get_service_accounts_using_get(application=application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->get_service_accounts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logged_out_using_get**
> str logged_out_using_get()

Get logged out message

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.AuthControllerApi()

try:
    # Get logged out message
    api_response = api_instance.logged_out_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->logged_out_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redirect_using_get**
> redirect_using_get(to)

Redirect to Deck

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.AuthControllerApi()
to = 'to_example' # str | to

try:
    # Redirect to Deck
    api_instance.redirect_using_get(to)
except ApiException as e:
    print("Exception when calling AuthControllerApi->redirect_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **str**| to | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_using_post**
> sync_using_post()

Sync user roles

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.AuthControllerApi()

try:
    # Sync user roles
    api_instance.sync_using_post()
except ApiException as e:
    print("Exception when calling AuthControllerApi->sync_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_using_get**
> User user_using_get()

Get user

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.AuthControllerApi()

try:
    # Get user
    api_response = api_instance.user_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->user_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

