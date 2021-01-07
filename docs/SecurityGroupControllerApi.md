# spinnaker-python-client.SecurityGroupControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_account_using_get1**](SecurityGroupControllerApi.md#all_by_account_using_get1) | **GET** /securityGroups/{account} | Retrieve a list of security groups for a given account, grouped by region
[**all_using_get5**](SecurityGroupControllerApi.md#all_using_get5) | **GET** /securityGroups | Retrieve a list of security groups, grouped by account, cloud provider, and region
[**get_security_group_using_get1**](SecurityGroupControllerApi.md#get_security_group_using_get1) | **GET** /securityGroups/{account}/{region}/{name} | Retrieve a security group&#39;s details


# **all_by_account_using_get1**
> object all_by_account_using_get1(account, x_rate_limit_app=x_rate_limit_app, provider=provider)

Retrieve a list of security groups for a given account, grouped by region

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.SecurityGroupControllerApi()
account = 'account_example' # str | account
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
provider = 'aws' # str | provider (optional) (default to aws)

try:
    # Retrieve a list of security groups for a given account, grouped by region
    api_response = api_instance.all_by_account_using_get1(account, x_rate_limit_app=x_rate_limit_app, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityGroupControllerApi->all_by_account_using_get1: %s\n" % e)
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

# **all_using_get5**
> object all_using_get5(x_rate_limit_app=x_rate_limit_app, id=id)

Retrieve a list of security groups, grouped by account, cloud provider, and region

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.SecurityGroupControllerApi()
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
id = 'id_example' # str | id (optional)

try:
    # Retrieve a list of security groups, grouped by account, cloud provider, and region
    api_response = api_instance.all_using_get5(x_rate_limit_app=x_rate_limit_app, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityGroupControllerApi->all_using_get5: %s\n" % e)
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

# **get_security_group_using_get1**
> object get_security_group_using_get1(account, name, region, x_rate_limit_app=x_rate_limit_app, provider=provider, vpc_id=vpc_id)

Retrieve a security group's details

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.SecurityGroupControllerApi()
account = 'account_example' # str | account
name = 'name_example' # str | name
region = 'region_example' # str | region
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
provider = 'aws' # str | provider (optional) (default to aws)
vpc_id = 'vpc_id_example' # str | vpcId (optional)

try:
    # Retrieve a security group's details
    api_response = api_instance.get_security_group_using_get1(account, name, region, x_rate_limit_app=x_rate_limit_app, provider=provider, vpc_id=vpc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityGroupControllerApi->get_security_group_using_get1: %s\n" % e)
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

