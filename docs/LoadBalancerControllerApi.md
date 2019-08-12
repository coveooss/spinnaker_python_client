# swagger_client.LoadBalancerControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_using_get**](LoadBalancerControllerApi.md#get_all_using_get) | **GET** /loadBalancers | Retrieve a list of load balancers for a given cloud provider
[**get_application_load_balancers_using_get**](LoadBalancerControllerApi.md#get_application_load_balancers_using_get) | **GET** /applications/{application}/loadBalancers | Retrieve a list of load balancers for a given application
[**get_load_balancer_details_using_get**](LoadBalancerControllerApi.md#get_load_balancer_details_using_get) | **GET** /loadBalancers/{account}/{region}/{name} | Retrieve a load balancer&#39;s details as a single element list for a given account, region, cloud provider and load balancer name
[**get_load_balancer_using_get**](LoadBalancerControllerApi.md#get_load_balancer_using_get) | **GET** /loadBalancers/{name} | Retrieve a load balancer for a given cloud provider


# **get_all_using_get**
> list[object] get_all_using_get(provider=provider, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of load balancers for a given cloud provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerControllerApi()
provider = 'aws' # str | provider (optional) (default to aws)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of load balancers for a given cloud provider
    api_response = api_instance.get_all_using_get(provider=provider, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerControllerApi->get_all_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_application_load_balancers_using_get**
> list[object] get_application_load_balancers_using_get(application, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of load balancers for a given application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerControllerApi()
application = 'application_example' # str | application
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of load balancers for a given application
    api_response = api_instance.get_application_load_balancers_using_get(application, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerControllerApi->get_application_load_balancers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_details_using_get**
> list[object] get_load_balancer_details_using_get(account, region, name, provider=provider, x_rate_limit_app=x_rate_limit_app)

Retrieve a load balancer's details as a single element list for a given account, region, cloud provider and load balancer name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerControllerApi()
account = 'account_example' # str | account
region = 'region_example' # str | region
name = 'name_example' # str | name
provider = 'aws' # str | provider (optional) (default to aws)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a load balancer's details as a single element list for a given account, region, cloud provider and load balancer name
    api_response = api_instance.get_load_balancer_details_using_get(account, region, name, provider=provider, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerControllerApi->get_load_balancer_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **region** | **str**| region | 
 **name** | **str**| name | 
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

# **get_load_balancer_using_get**
> dict(str, object) get_load_balancer_using_get(name, provider=provider, x_rate_limit_app=x_rate_limit_app)

Retrieve a load balancer for a given cloud provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerControllerApi()
name = 'name_example' # str | name
provider = 'aws' # str | provider (optional) (default to aws)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a load balancer for a given cloud provider
    api_response = api_instance.get_load_balancer_using_get(name, provider=provider, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerControllerApi->get_load_balancer_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **provider** | **str**| provider | [optional] [default to aws]
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

