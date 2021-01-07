# spinnaker-python-client.ImageControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_images_using_get**](ImageControllerApi.md#find_images_using_get) | **GET** /images/find | Retrieve a list of images, filtered by cloud provider, region, and account
[**find_tags_using_get**](ImageControllerApi.md#find_tags_using_get) | **GET** /images/tags | Find tags
[**get_image_details_using_get**](ImageControllerApi.md#get_image_details_using_get) | **GET** /images/{account}/{region}/{imageId} | Get image details


# **find_images_using_get**
> list[object] find_images_using_get(account=account, count=count, provider=provider, q=q, region=region)

Retrieve a list of images, filtered by cloud provider, region, and account

The query parameter `q` filters the list of images by image name

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.ImageControllerApi()
account = 'account_example' # str | account (optional)
count = 56 # int | count (optional)
provider = 'aws' # str | provider (optional) (default to aws)
q = 'q_example' # str | q (optional)
region = 'region_example' # str | region (optional)

try:
    # Retrieve a list of images, filtered by cloud provider, region, and account
    api_response = api_instance.find_images_using_get(account=account, count=count, provider=provider, q=q, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageControllerApi->find_images_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | [optional] 
 **count** | **int**| count | [optional] 
 **provider** | **str**| provider | [optional] [default to aws]
 **q** | **str**| q | [optional] 
 **region** | **str**| region | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tags_using_get**
> list[object] find_tags_using_get(account, repository, x_rate_limit_app=x_rate_limit_app, provider=provider)

Find tags

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.ImageControllerApi()
account = 'account_example' # str | account
repository = 'repository_example' # str | repository
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
provider = 'aws' # str | provider (optional) (default to aws)

try:
    # Find tags
    api_response = api_instance.find_tags_using_get(account, repository, x_rate_limit_app=x_rate_limit_app, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageControllerApi->find_tags_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **repository** | **str**| repository | 
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

# **get_image_details_using_get**
> list[object] get_image_details_using_get(account, image_id, region, x_rate_limit_app=x_rate_limit_app, provider=provider)

Get image details

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.ImageControllerApi()
account = 'account_example' # str | account
image_id = 'image_id_example' # str | imageId
region = 'region_example' # str | region
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
provider = 'aws' # str | provider (optional) (default to aws)

try:
    # Get image details
    api_response = api_instance.get_image_details_using_get(account, image_id, region, x_rate_limit_app=x_rate_limit_app, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageControllerApi->get_image_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **image_id** | **str**| imageId | 
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

