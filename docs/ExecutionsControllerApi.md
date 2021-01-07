# spinnaker-python-client.ExecutionsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_executions_by_config_ids_using_get**](ExecutionsControllerApi.md#get_latest_executions_by_config_ids_using_get) | **GET** /executions | Retrieves an ad-hoc collection of executions based on a number of user-supplied parameters. Either executionIds or pipelineConfigIds must be supplied in order to return any results. If both are supplied, an exception will be thrown.
[**search_for_pipeline_executions_by_trigger_using_get**](ExecutionsControllerApi.md#search_for_pipeline_executions_by_trigger_using_get) | **GET** /applications/{application}/executions/search | Search for pipeline executions using a combination of criteria. The returned list is sorted by buildTime (trigger time) in reverse order so that newer executions are first in the list.


# **get_latest_executions_by_config_ids_using_get**
> list[object] get_latest_executions_by_config_ids_using_get(execution_ids=execution_ids, expand=expand, limit=limit, pipeline_config_ids=pipeline_config_ids, statuses=statuses)

Retrieves an ad-hoc collection of executions based on a number of user-supplied parameters. Either executionIds or pipelineConfigIds must be supplied in order to return any results. If both are supplied, an exception will be thrown.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.ExecutionsControllerApi()
execution_ids = 'execution_ids_example' # str | A comma-separated list of executions to retrieve. Either this OR pipelineConfigIds must be supplied, but not both. (optional)
expand = true # bool | Expands each execution object in the resulting list. If this value is missing, it is defaulted to true. (optional) (default to true)
limit = 56 # int | The number of executions to return per pipeline configuration. Ignored if executionIds parameter is supplied. If this value is missing, it is defaulted to 1. (optional)
pipeline_config_ids = 'pipeline_config_ids_example' # str | A comma-separated list of pipeline configuration IDs to retrieve recent executions for. Either this OR pipelineConfigIds must be supplied, but not both. (optional)
statuses = 'statuses_example' # str | A comma-separated list of execution statuses to filter by. Ignored if executionIds parameter is supplied. If this value is missing, it is defaulted to all statuses. (optional)

try:
    # Retrieves an ad-hoc collection of executions based on a number of user-supplied parameters. Either executionIds or pipelineConfigIds must be supplied in order to return any results. If both are supplied, an exception will be thrown.
    api_response = api_instance.get_latest_executions_by_config_ids_using_get(execution_ids=execution_ids, expand=expand, limit=limit, pipeline_config_ids=pipeline_config_ids, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecutionsControllerApi->get_latest_executions_by_config_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_ids** | **str**| A comma-separated list of executions to retrieve. Either this OR pipelineConfigIds must be supplied, but not both. | [optional] 
 **expand** | **bool**| Expands each execution object in the resulting list. If this value is missing, it is defaulted to true. | [optional] [default to true]
 **limit** | **int**| The number of executions to return per pipeline configuration. Ignored if executionIds parameter is supplied. If this value is missing, it is defaulted to 1. | [optional] 
 **pipeline_config_ids** | **str**| A comma-separated list of pipeline configuration IDs to retrieve recent executions for. Either this OR pipelineConfigIds must be supplied, but not both. | [optional] 
 **statuses** | **str**| A comma-separated list of execution statuses to filter by. Ignored if executionIds parameter is supplied. If this value is missing, it is defaulted to all statuses. | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_for_pipeline_executions_by_trigger_using_get**
> list[object] search_for_pipeline_executions_by_trigger_using_get(application, event_id=event_id, expand=expand, pipeline_name=pipeline_name, reverse=reverse, size=size, start_index=start_index, statuses=statuses, trigger=trigger, trigger_time_end_boundary=trigger_time_end_boundary, trigger_time_start_boundary=trigger_time_start_boundary, trigger_types=trigger_types)

Search for pipeline executions using a combination of criteria. The returned list is sorted by buildTime (trigger time) in reverse order so that newer executions are first in the list.

### Example
```python
from __future__ import print_function
import time
import spinnaker-python-client
from spinnaker-python-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker-python-client.ExecutionsControllerApi()
application = 'application_example' # str | Only includes executions that are part of this application. If this value is \"*\", results will include executions of all applications.
event_id = 'event_id_example' # str | Only includes executions that were triggered by a trigger with this eventId. (optional)
expand = false # bool | Expands each execution object in the resulting list. If this value is missing, it is defaulted to false. (optional) (default to false)
pipeline_name = 'pipeline_name_example' # str | Only includes executions that with this pipeline name. (optional)
reverse = false # bool | Reverses the resulting list before it is paginated. If this value is missing, it is defaulted to false. (optional) (default to false)
size = 10 # int | Sets the size of the resulting list for pagination. This value must be > 0. If this value is missing, it is defaulted to 10. (optional) (default to 10)
start_index = 0 # int | Sets the first item of the resulting list for pagination. The list is 0-indexed. This value must be >= 0. If this value is missing, it is defaulted to 0. (optional) (default to 0)
statuses = 'statuses_example' # str | Only includes executions with a status that is equal to a status provided in this field. The list of statuses should be given as a comma-delimited string. If this value is missing, includes executions of all statuses. Allowed statuses are: NOT_STARTED, RUNNING, PAUSED, SUSPENDED, SUCCEEDED, FAILED_CONTINUE, TERMINAL, CANCELED, REDIRECT, STOPPED, SKIPPED, BUFFERED. (optional)
trigger = 'trigger_example' # str | Only includes executions that were triggered by a trigger that matches the subset of fields provided by this value. This value should be a base64-encoded string of a JSON representation of a trigger object. The comparison succeeds if the execution trigger contains all the fields of the input trigger, the fields are of the same type, and each value of the field \"matches\". The term \"matches\" is specific for each field's type: - For Strings: A String value in the execution's trigger matches the input trigger's String value if the former equals the latter (case-insensitive) OR if the former matches the latter as a regular expression. - For Maps: A Map value in the execution's trigger matches the input trigger's Map value if the former contains all keys of the latter and their values match. - For Collections: A Collection value in the execution's trigger matches the input trigger's Collection value if the former has a unique element that matches each element of the latter. - Every other value is compared using the Java \"equals\" method (Groovy \"==\" operator) (optional)
trigger_time_end_boundary = 789 # int | Only includes executions that were built at or before the given time, represented as a Unix timestamp in ms (UTC). This value must be <= 9223372036854775807 (Long.MAX_VALUE) and >= the value of [triggerTimeStartBoundary], if provided. If this value is missing, it is defaulted to 9223372036854775807. (optional)
trigger_time_start_boundary = 0 # int | Only includes executions that were built at or after the given time, represented as a Unix timestamp in ms (UTC). This value must be >= 0 and <= the value of [triggerTimeEndBoundary], if provided. If this value is missing, it is defaulted to 0. (optional) (default to 0)
trigger_types = 'trigger_types_example' # str | Only includes executions that were triggered by a trigger with a type that is equal to a type provided in this field. The list of trigger types should be a comma-delimited string. If this value is missing, results will includes executions of all trigger types. (optional)

try:
    # Search for pipeline executions using a combination of criteria. The returned list is sorted by buildTime (trigger time) in reverse order so that newer executions are first in the list.
    api_response = api_instance.search_for_pipeline_executions_by_trigger_using_get(application, event_id=event_id, expand=expand, pipeline_name=pipeline_name, reverse=reverse, size=size, start_index=start_index, statuses=statuses, trigger=trigger, trigger_time_end_boundary=trigger_time_end_boundary, trigger_time_start_boundary=trigger_time_start_boundary, trigger_types=trigger_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecutionsControllerApi->search_for_pipeline_executions_by_trigger_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| Only includes executions that are part of this application. If this value is \&quot;*\&quot;, results will include executions of all applications. | 
 **event_id** | **str**| Only includes executions that were triggered by a trigger with this eventId. | [optional] 
 **expand** | **bool**| Expands each execution object in the resulting list. If this value is missing, it is defaulted to false. | [optional] [default to false]
 **pipeline_name** | **str**| Only includes executions that with this pipeline name. | [optional] 
 **reverse** | **bool**| Reverses the resulting list before it is paginated. If this value is missing, it is defaulted to false. | [optional] [default to false]
 **size** | **int**| Sets the size of the resulting list for pagination. This value must be &gt; 0. If this value is missing, it is defaulted to 10. | [optional] [default to 10]
 **start_index** | **int**| Sets the first item of the resulting list for pagination. The list is 0-indexed. This value must be &gt;&#x3D; 0. If this value is missing, it is defaulted to 0. | [optional] [default to 0]
 **statuses** | **str**| Only includes executions with a status that is equal to a status provided in this field. The list of statuses should be given as a comma-delimited string. If this value is missing, includes executions of all statuses. Allowed statuses are: NOT_STARTED, RUNNING, PAUSED, SUSPENDED, SUCCEEDED, FAILED_CONTINUE, TERMINAL, CANCELED, REDIRECT, STOPPED, SKIPPED, BUFFERED. | [optional] 
 **trigger** | **str**| Only includes executions that were triggered by a trigger that matches the subset of fields provided by this value. This value should be a base64-encoded string of a JSON representation of a trigger object. The comparison succeeds if the execution trigger contains all the fields of the input trigger, the fields are of the same type, and each value of the field \&quot;matches\&quot;. The term \&quot;matches\&quot; is specific for each field&#39;s type: - For Strings: A String value in the execution&#39;s trigger matches the input trigger&#39;s String value if the former equals the latter (case-insensitive) OR if the former matches the latter as a regular expression. - For Maps: A Map value in the execution&#39;s trigger matches the input trigger&#39;s Map value if the former contains all keys of the latter and their values match. - For Collections: A Collection value in the execution&#39;s trigger matches the input trigger&#39;s Collection value if the former has a unique element that matches each element of the latter. - Every other value is compared using the Java \&quot;equals\&quot; method (Groovy \&quot;&#x3D;&#x3D;\&quot; operator) | [optional] 
 **trigger_time_end_boundary** | **int**| Only includes executions that were built at or before the given time, represented as a Unix timestamp in ms (UTC). This value must be &lt;&#x3D; 9223372036854775807 (Long.MAX_VALUE) and &gt;&#x3D; the value of [triggerTimeStartBoundary], if provided. If this value is missing, it is defaulted to 9223372036854775807. | [optional] 
 **trigger_time_start_boundary** | **int**| Only includes executions that were built at or after the given time, represented as a Unix timestamp in ms (UTC). This value must be &gt;&#x3D; 0 and &lt;&#x3D; the value of [triggerTimeEndBoundary], if provided. If this value is missing, it is defaulted to 0. | [optional] [default to 0]
 **trigger_types** | **str**| Only includes executions that were triggered by a trigger with a type that is equal to a type provided in this field. The list of trigger types should be a comma-delimited string. If this value is missing, results will includes executions of all trigger types. | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

