# spinnaker-python-client.FirewallControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_account_and_region_using_get**](FirewallControllerApi.md#all_by_account_and_region_using_get) | **GET** /firewalls/{account}/{region} | Retrieve a list of firewalls for a given account and region
[**all_by_account_using_get**](FirewallControllerApi.md#all_by_account_using_get) | **GET** /firewalls/{account} | Retrieve a list of firewalls for a given account, grouped by region
[**all_using_get1**](FirewallControllerApi.md#all_using_get1) | **GET** /firewalls | Retrieve a list of firewalls, grouped by account, cloud provider, and region
[**get_security_group_using_get**](FirewallControllerApi.md#get_security_group_using_get) | **GET** /firewalls/{account}/{region}/{name} | Retrieve a firewall&#39;s details


# **all_by_account_and_region_using_get**
> list[object] all_by_account_and_region_using_get(account, region, x_rate_limit_app=x_rate_limit_app, provider=provider)

Retrieve a list of firewalls for a given account and region

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.FirewallControllerApi()
account = 'account_example' # str | account
region = 'region_example' # str | region
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
provider = 'aws' # str | provider (optional) (default to aws)

try:
    # Retrieve a list of firewalls for a given account and region
    api_response = api_instance.all_by_account_and_region_using_get(account, region, x_rate_limit_app=x_rate_limit_app, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallControllerApi->all_by_account_and_region_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **region** | **str**| region | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **provider** | **str**| provider | [optional] [default to aws]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_by_account_using_get**
> object all_by_account_using_get(account, x_rate_limit_app=x_rate_limit_app, provider=provider)

Retrieve a list of firewalls for a given account, grouped by region

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.FirewallControllerApi()
account = 'account_example' # str | account
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
provider = 'aws' # str | provider (optional) (default to aws)

try:
    # Retrieve a list of firewalls for a given account, grouped by region
    api_response = api_instance.all_by_account_using_get(account, x_rate_limit_app=x_rate_limit_app, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallControllerApi->all_by_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **provider** | **str**| provider | [optional] [default to aws]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_using_get1**
> object all_using_get1(x_rate_limit_app=x_rate_limit_app, id=id)

Retrieve a list of firewalls, grouped by account, cloud provider, and region

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.FirewallControllerApi()
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
id = 'id_example' # str | id (optional)

try:
    # Retrieve a list of firewalls, grouped by account, cloud provider, and region
    api_response = api_instance.all_using_get1(x_rate_limit_app=x_rate_limit_app, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallControllerApi->all_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **id** | **str**| id | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_group_using_get**
> object get_security_group_using_get(account, name, region, x_rate_limit_app=x_rate_limit_app, provider=provider, vpc_id=vpc_id)

Retrieve a firewall's details

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.FirewallControllerApi()
account = 'account_example' # str | account
name = 'name_example' # str | name
region = 'region_example' # str | region
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
provider = 'aws' # str | provider (optional) (default to aws)
vpc_id = 'vpc_id_example' # str | vpcId (optional)

try:
    # Retrieve a firewall's details
    api_response = api_instance.get_security_group_using_get(account, name, region, x_rate_limit_app=x_rate_limit_app, provider=provider, vpc_id=vpc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallControllerApi->get_security_group_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **name** | **str**| name | 
 **region** | **str**| region | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **provider** | **str**| provider | [optional] [default to aws]
 **vpc_id** | **str**| vpcId | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

