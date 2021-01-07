# spinnaker_swagger_client.CredentialsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_using_get**](CredentialsControllerApi.md#get_account_using_get) | **GET** /credentials/{account} | Retrieve an account&#39;s details
[**get_accounts_using_get**](CredentialsControllerApi.md#get_accounts_using_get) | **GET** /credentials | Retrieve a list of accounts


# **get_account_using_get**
> AccountDetails get_account_using_get(account, x_rate_limit_app=x_rate_limit_app, account_non_expired=account_non_expired, account_non_locked=account_non_locked, allowed_accounts=allowed_accounts, authorities_0_authority=authorities_0_authority, credentials_non_expired=credentials_non_expired, email=email, enabled=enabled, first_name=first_name, last_name=last_name, password=password, roles=roles, username=username)

Retrieve an account's details

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.CredentialsControllerApi()
account = 'account_example' # str | account
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
account_non_expired = true # bool |  (optional)
account_non_locked = true # bool |  (optional)
allowed_accounts = ['allowed_accounts_example'] # list[str] |  (optional)
authorities_0_authority = 'authorities_0_authority_example' # str |  (optional)
credentials_non_expired = true # bool |  (optional)
email = 'email_example' # str |  (optional)
enabled = true # bool |  (optional)
first_name = 'first_name_example' # str |  (optional)
last_name = 'last_name_example' # str |  (optional)
password = 'password_example' # str |  (optional)
roles = ['roles_example'] # list[str] |  (optional)
username = 'username_example' # str |  (optional)

try:
    # Retrieve an account's details
    api_response = api_instance.get_account_using_get(account, x_rate_limit_app=x_rate_limit_app, account_non_expired=account_non_expired, account_non_locked=account_non_locked, allowed_accounts=allowed_accounts, authorities_0_authority=authorities_0_authority, credentials_non_expired=credentials_non_expired, email=email, enabled=enabled, first_name=first_name, last_name=last_name, password=password, roles=roles, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsControllerApi->get_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **account_non_expired** | **bool**|  | [optional] 
 **account_non_locked** | **bool**|  | [optional] 
 **allowed_accounts** | [**list[str]**](str.md)|  | [optional] 
 **authorities_0_authority** | **str**|  | [optional] 
 **credentials_non_expired** | **bool**|  | [optional] 
 **email** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **first_name** | **str**|  | [optional] 
 **last_name** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **roles** | [**list[str]**](str.md)|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**AccountDetails**](AccountDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_using_get**
> list[Account] get_accounts_using_get(account_non_expired=account_non_expired, account_non_locked=account_non_locked, allowed_accounts=allowed_accounts, authorities_0_authority=authorities_0_authority, credentials_non_expired=credentials_non_expired, email=email, enabled=enabled, expand=expand, first_name=first_name, last_name=last_name, password=password, roles=roles, username=username)

Retrieve a list of accounts

### Example
```python
from __future__ import print_function
import time
import spinnaker_swagger_client
from spinnaker_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_swagger_client.CredentialsControllerApi()
account_non_expired = true # bool |  (optional)
account_non_locked = true # bool |  (optional)
allowed_accounts = ['allowed_accounts_example'] # list[str] |  (optional)
authorities_0_authority = 'authorities_0_authority_example' # str |  (optional)
credentials_non_expired = true # bool |  (optional)
email = 'email_example' # str |  (optional)
enabled = true # bool |  (optional)
expand = true # bool | expand (optional)
first_name = 'first_name_example' # str |  (optional)
last_name = 'last_name_example' # str |  (optional)
password = 'password_example' # str |  (optional)
roles = ['roles_example'] # list[str] |  (optional)
username = 'username_example' # str |  (optional)

try:
    # Retrieve a list of accounts
    api_response = api_instance.get_accounts_using_get(account_non_expired=account_non_expired, account_non_locked=account_non_locked, allowed_accounts=allowed_accounts, authorities_0_authority=authorities_0_authority, credentials_non_expired=credentials_non_expired, email=email, enabled=enabled, expand=expand, first_name=first_name, last_name=last_name, password=password, roles=roles, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsControllerApi->get_accounts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_non_expired** | **bool**|  | [optional] 
 **account_non_locked** | **bool**|  | [optional] 
 **allowed_accounts** | [**list[str]**](str.md)|  | [optional] 
 **authorities_0_authority** | **str**|  | [optional] 
 **credentials_non_expired** | **bool**|  | [optional] 
 **email** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **expand** | **bool**| expand | [optional] 
 **first_name** | **str**|  | [optional] 
 **last_name** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **roles** | [**list[str]**](str.md)|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**list[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

