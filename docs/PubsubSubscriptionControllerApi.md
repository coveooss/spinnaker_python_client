# spinnaker-python-client.PubsubSubscriptionControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_using_get4**](PubsubSubscriptionControllerApi.md#all_using_get4) | **GET** /pubsub/subscriptions | Retrieve the list of pub/sub subscriptions configured in Echo.


# **all_using_get4**
> list[Mapstringstring] all_using_get4()

Retrieve the list of pub/sub subscriptions configured in Echo.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.PubsubSubscriptionControllerApi()

try:
    # Retrieve the list of pub/sub subscriptions configured in Echo.
    api_response = api_instance.all_using_get4()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubsubSubscriptionControllerApi->all_using_get4: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Mapstringstring]**](Mapstringstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

