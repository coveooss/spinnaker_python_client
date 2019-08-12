# swagger_client.ImageControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_images_using_get**](ImageControllerApi.md#find_images_using_get) | **GET** /images/find | Retrieve a list of images, filtered by cloud provider, region, and account
[**find_tags_using_get**](ImageControllerApi.md#find_tags_using_get) | **GET** /images/tags | Find tags
[**get_image_details_using_get**](ImageControllerApi.md#get_image_details_using_get) | **GET** /images/{account}/{region}/{imageId} | Get image details


# **find_images_using_get**
> list[object] find_images_using_get(provider=provider, q=q, region=region, account=account, count=count)

Retrieve a list of images, filtered by cloud provider, region, and account

The query parameter `q` filters the list of images by image name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageControllerApi()
provider = 'aws' # str | provider (optional) (default to aws)
q = 'q_example' # str | q (optional)
region = 'region_example' # str | region (optional)
account = 'account_example' # str | account (optional)
count = 56 # int | count (optional)

try:
    # Retrieve a list of images, filtered by cloud provider, region, and account
    api_response = api_instance.find_images_using_get(provider=provider, q=q, region=region, account=account, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageControllerApi->find_images_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| provider | [optional] [default to aws]
 **q** | **str**| q | [optional] 
 **region** | **str**| region | [optional] 
 **account** | **str**| account | [optional] 
 **count** | **int**| count | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tags_using_get**
> list[object] find_tags_using_get(account, repository, provider=provider, x_rate_limit_app=x_rate_limit_app)

Find tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageControllerApi()
account = 'account_example' # str | account
repository = 'repository_example' # str | repository
provider = 'aws' # str | provider (optional) (default to aws)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Find tags
    api_response = api_instance.find_tags_using_get(account, repository, provider=provider, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageControllerApi->find_tags_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **repository** | **str**| repository | 
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

# **get_image_details_using_get**
> list[object] get_image_details_using_get(account, region, image_id, provider=provider, x_rate_limit_app=x_rate_limit_app)

Get image details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageControllerApi()
account = 'account_example' # str | account
region = 'region_example' # str | region
image_id = 'image_id_example' # str | imageId
provider = 'aws' # str | provider (optional) (default to aws)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Get image details
    api_response = api_instance.get_image_details_using_get(account, region, image_id, provider=provider, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageControllerApi->get_image_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **region** | **str**| region | 
 **image_id** | **str**| imageId | 
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

