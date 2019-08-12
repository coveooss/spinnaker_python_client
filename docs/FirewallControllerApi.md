# swagger_client.FirewallControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_account_and_region_using_get**](FirewallControllerApi.md#all_by_account_and_region_using_get) | **GET** /firewalls/{account}/{region} | Retrieve a list of firewalls for a given account and region
[**all_by_account_using_get**](FirewallControllerApi.md#all_by_account_using_get) | **GET** /firewalls/{account} | Retrieve a list of firewalls for a given account, grouped by region
[**all_using_get1**](FirewallControllerApi.md#all_using_get1) | **GET** /firewalls | Retrieve a list of firewalls, grouped by account, cloud provider, and region
[**get_security_group_using_get**](FirewallControllerApi.md#get_security_group_using_get) | **GET** /firewalls/{account}/{region}/{name} | Retrieve a firewall&#39;s details


# **all_by_account_and_region_using_get**
> list[object] all_by_account_and_region_using_get(account, region, provider=provider, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of firewalls for a given account and region

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallControllerApi()
account = 'account_example' # str | account
region = 'region_example' # str | region
provider = 'aws' # str | provider (optional) (default to aws)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of firewalls for a given account and region
    api_response = api_instance.all_by_account_and_region_using_get(account, region, provider=provider, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallControllerApi->all_by_account_and_region_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **region** | **str**| region | 
 **provider** | **str**| provider | [optional] [default to aws]
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_by_account_using_get**
> object all_by_account_using_get(account, provider=provider, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of firewalls for a given account, grouped by region

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallControllerApi()
account = 'account_example' # str | account
provider = 'aws' # str | provider (optional) (default to aws)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of firewalls for a given account, grouped by region
    api_response = api_instance.all_by_account_using_get(account, provider=provider, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallControllerApi->all_by_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **provider** | **str**| provider | [optional] [default to aws]
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_using_get1**
> object all_using_get1(id=id, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of firewalls, grouped by account, cloud provider, and region

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallControllerApi()
id = 'id_example' # str | id (optional)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of firewalls, grouped by account, cloud provider, and region
    api_response = api_instance.all_using_get1(id=id, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallControllerApi->all_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | [optional] 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_group_using_get**
> object get_security_group_using_get(account, region, name, provider=provider, vpc_id=vpc_id, x_rate_limit_app=x_rate_limit_app)

Retrieve a firewall's details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallControllerApi()
account = 'account_example' # str | account
region = 'region_example' # str | region
name = 'name_example' # str | name
provider = 'aws' # str | provider (optional) (default to aws)
vpc_id = 'vpc_id_example' # str | vpcId (optional)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a firewall's details
    api_response = api_instance.get_security_group_using_get(account, region, name, provider=provider, vpc_id=vpc_id, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallControllerApi->get_security_group_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **region** | **str**| region | 
 **name** | **str**| name | 
 **provider** | **str**| provider | [optional] [default to aws]
 **vpc_id** | **str**| vpcId | [optional] 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

