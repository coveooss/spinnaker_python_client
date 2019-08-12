# swagger_client.BuildControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build_masters_using_get**](BuildControllerApi.md#get_build_masters_using_get) | **GET** /v2/builds | Get build masters
[**get_build_using_get**](BuildControllerApi.md#get_build_using_get) | **GET** /v2/builds/{buildMaster}/build/{number}/** | Get build for build master
[**get_builds_using_get**](BuildControllerApi.md#get_builds_using_get) | **GET** /v2/builds/{buildMaster}/builds/** | Get builds for build master
[**get_job_config_using_get**](BuildControllerApi.md#get_job_config_using_get) | **GET** /v2/builds/{buildMaster}/jobs/** | Get job config
[**get_jobs_for_build_master_using_get**](BuildControllerApi.md#get_jobs_for_build_master_using_get) | **GET** /v2/builds/{buildMaster}/jobs | Get jobs for build master
[**v3_get_build_masters_using_get**](BuildControllerApi.md#v3_get_build_masters_using_get) | **GET** /v3/builds | Get build masters
[**v3_get_build_using_get**](BuildControllerApi.md#v3_get_build_using_get) | **GET** /v3/builds/{buildMaster}/build/{number} | Get build for build master
[**v3_get_builds_using_get**](BuildControllerApi.md#v3_get_builds_using_get) | **GET** /v3/builds/{buildMaster}/builds | Get builds for build master
[**v3_get_job_config_using_get**](BuildControllerApi.md#v3_get_job_config_using_get) | **GET** /v3/builds/{buildMaster}/job | Get job config
[**v3_get_jobs_for_build_master_using_get**](BuildControllerApi.md#v3_get_jobs_for_build_master_using_get) | **GET** /v3/builds/{buildMaster}/jobs | Get jobs for build master


# **get_build_masters_using_get**
> list[object] get_build_masters_using_get(type)

Get build masters

Deprecated, use the v3 endpoint instead

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
type = 'type_example' # str | type

try:
    # Get build masters
    api_response = api_instance.get_build_masters_using_get(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->get_build_masters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_using_get**
> dict(str, object) get_build_using_get(build_master, number)

Get build for build master

Deprecated, use the v3 endpoint instead

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
build_master = 'build_master_example' # str | buildMaster
number = 'number_example' # str | number

try:
    # Get build for build master
    api_response = api_instance.get_build_using_get(build_master, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->get_build_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 
 **number** | **str**| number | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds_using_get**
> list[object] get_builds_using_get(build_master)

Get builds for build master

Deprecated, use the v3 endpoint instead

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
build_master = 'build_master_example' # str | buildMaster

try:
    # Get builds for build master
    api_response = api_instance.get_builds_using_get(build_master)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->get_builds_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_config_using_get**
> dict(str, object) get_job_config_using_get(build_master)

Get job config

Deprecated, use the v3 endpoint instead

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
build_master = 'build_master_example' # str | buildMaster

try:
    # Get job config
    api_response = api_instance.get_job_config_using_get(build_master)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->get_job_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_for_build_master_using_get**
> list[object] get_jobs_for_build_master_using_get(build_master)

Get jobs for build master

Deprecated, use the v3 endpoint instead

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
build_master = 'build_master_example' # str | buildMaster

try:
    # Get jobs for build master
    api_response = api_instance.get_jobs_for_build_master_using_get(build_master)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->get_jobs_for_build_master_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_build_masters_using_get**
> list[object] v3_get_build_masters_using_get(type)

Get build masters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
type = 'type_example' # str | type

try:
    # Get build masters
    api_response = api_instance.v3_get_build_masters_using_get(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->v3_get_build_masters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_build_using_get**
> dict(str, object) v3_get_build_using_get(build_master, number, job)

Get build for build master

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
build_master = 'build_master_example' # str | buildMaster
number = 'number_example' # str | number
job = 'job_example' # str | job

try:
    # Get build for build master
    api_response = api_instance.v3_get_build_using_get(build_master, number, job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->v3_get_build_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 
 **number** | **str**| number | 
 **job** | **str**| job | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_builds_using_get**
> list[object] v3_get_builds_using_get(build_master, job)

Get builds for build master

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
build_master = 'build_master_example' # str | buildMaster
job = 'job_example' # str | job

try:
    # Get builds for build master
    api_response = api_instance.v3_get_builds_using_get(build_master, job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->v3_get_builds_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 
 **job** | **str**| job | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_job_config_using_get**
> dict(str, object) v3_get_job_config_using_get(build_master, job)

Get job config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
build_master = 'build_master_example' # str | buildMaster
job = 'job_example' # str | job

try:
    # Get job config
    api_response = api_instance.v3_get_job_config_using_get(build_master, job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->v3_get_job_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 
 **job** | **str**| job | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_jobs_for_build_master_using_get**
> list[object] v3_get_jobs_for_build_master_using_get(build_master)

Get jobs for build master

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildControllerApi()
build_master = 'build_master_example' # str | buildMaster

try:
    # Get jobs for build master
    api_response = api_instance.v3_get_jobs_for_build_master_using_get(build_master)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->v3_get_jobs_for_build_master_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_master** | **str**| buildMaster | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

