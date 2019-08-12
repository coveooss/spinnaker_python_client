# swagger_client.CredentialsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_using_get**](CredentialsControllerApi.md#get_account_using_get) | **GET** /credentials/{account} | Retrieve an account&#39;s details
[**get_accounts_using_get**](CredentialsControllerApi.md#get_accounts_using_get) | **GET** /credentials | Retrieve a list of accounts


# **get_account_using_get**
> AccountDetails get_account_using_get(account, roles=roles, allowed_accounts=allowed_accounts, email=email, username=username, first_name=first_name, last_name=last_name, x_rate_limit_app=x_rate_limit_app)

Retrieve an account's details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialsControllerApi()
account = 'account_example' # str | account
roles = ['roles_example'] # list[str] |  (optional)
allowed_accounts = ['allowed_accounts_example'] # list[str] |  (optional)
email = 'email_example' # str |  (optional)
username = 'username_example' # str |  (optional)
first_name = 'first_name_example' # str |  (optional)
last_name = 'last_name_example' # str |  (optional)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve an account's details
    api_response = api_instance.get_account_using_get(account, roles=roles, allowed_accounts=allowed_accounts, email=email, username=username, first_name=first_name, last_name=last_name, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsControllerApi->get_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **roles** | [**list[str]**](str.md)|  | [optional] 
 **allowed_accounts** | [**list[str]**](str.md)|  | [optional] 
 **email** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **first_name** | **str**|  | [optional] 
 **last_name** | **str**|  | [optional] 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

[**AccountDetails**](AccountDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_using_get**
> list[Account] get_accounts_using_get(roles=roles, allowed_accounts=allowed_accounts, email=email, username=username, first_name=first_name, last_name=last_name, expand=expand)

Retrieve a list of accounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialsControllerApi()
roles = ['roles_example'] # list[str] |  (optional)
allowed_accounts = ['allowed_accounts_example'] # list[str] |  (optional)
email = 'email_example' # str |  (optional)
username = 'username_example' # str |  (optional)
first_name = 'first_name_example' # str |  (optional)
last_name = 'last_name_example' # str |  (optional)
expand = true # bool | expand (optional)

try:
    # Retrieve a list of accounts
    api_response = api_instance.get_accounts_using_get(roles=roles, allowed_accounts=allowed_accounts, email=email, username=username, first_name=first_name, last_name=last_name, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsControllerApi->get_accounts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles** | [**list[str]**](str.md)|  | [optional] 
 **allowed_accounts** | [**list[str]**](str.md)|  | [optional] 
 **email** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **first_name** | **str**|  | [optional] 
 **last_name** | **str**|  | [optional] 
 **expand** | **bool**| expand | [optional] 

### Return type

[**list[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

