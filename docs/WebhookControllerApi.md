# spinnaker-python-client.WebhookControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preconfigured_webhooks_using_get**](WebhookControllerApi.md#preconfigured_webhooks_using_get) | **GET** /webhooks/preconfigured | Retrieve a list of preconfigured webhooks in Orca
[**webhooks_using_post**](WebhookControllerApi.md#webhooks_using_post) | **POST** /webhooks/{type}/{source} | Endpoint for posting webhooks to Spinnaker&#39;s webhook service


# **preconfigured_webhooks_using_get**
> list[object] preconfigured_webhooks_using_get()

Retrieve a list of preconfigured webhooks in Orca

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.WebhookControllerApi()

try:
    # Retrieve a list of preconfigured webhooks in Orca
    api_response = api_instance.preconfigured_webhooks_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookControllerApi->preconfigured_webhooks_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_using_post**
> object webhooks_using_post(source, type, x_event_key=x_event_key, x_hub_signature=x_hub_signature, event=event)

Endpoint for posting webhooks to Spinnaker's webhook service

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.WebhookControllerApi()
source = 'source_example' # str | source
type = 'type_example' # str | type
x_event_key = 'x_event_key_example' # str | X-Event-Key (optional)
x_hub_signature = 'x_hub_signature_example' # str | X-Hub-Signature (optional)
event = NULL # object | event (optional)

try:
    # Endpoint for posting webhooks to Spinnaker's webhook service
    api_response = api_instance.webhooks_using_post(source, type, x_event_key=x_event_key, x_hub_signature=x_hub_signature, event=event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookControllerApi->webhooks_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| source | 
 **type** | **str**| type | 
 **x_event_key** | **str**| X-Event-Key | [optional] 
 **x_hub_signature** | **str**| X-Hub-Signature | [optional] 
 **event** | **object**| event | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

