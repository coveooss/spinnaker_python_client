# swagger_client.ClusterControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_load_balancers_using_get**](ClusterControllerApi.md#get_cluster_load_balancers_using_get) | **GET** /applications/{application}/clusters/{account}/{clusterName}/{type}/loadBalancers | Retrieve a cluster&#39;s loadbalancers
[**get_clusters_using_get**](ClusterControllerApi.md#get_clusters_using_get) | **GET** /applications/{application}/clusters/{account}/{clusterName} | Retrieve a cluster&#39;s details
[**get_clusters_using_get1**](ClusterControllerApi.md#get_clusters_using_get1) | **GET** /applications/{application}/clusters/{account} | Retrieve a list of clusters for an account
[**get_clusters_using_get2**](ClusterControllerApi.md#get_clusters_using_get2) | **GET** /applications/{application}/clusters | Retrieve a list of cluster names for an application, grouped by account
[**get_scaling_activities_using_get**](ClusterControllerApi.md#get_scaling_activities_using_get) | **GET** /applications/{application}/clusters/{account}/{clusterName}/serverGroups/{serverGroupName}/scalingActivities | Retrieve a list of scaling activities for a server group
[**get_server_groups_using_get**](ClusterControllerApi.md#get_server_groups_using_get) | **GET** /applications/{application}/clusters/{account}/{clusterName}/serverGroups/{serverGroupName} | Retrieve a server group&#39;s details
[**get_server_groups_using_get1**](ClusterControllerApi.md#get_server_groups_using_get1) | **GET** /applications/{application}/clusters/{account}/{clusterName}/serverGroups | Retrieve a list of server groups for a cluster
[**get_target_server_group_using_get**](ClusterControllerApi.md#get_target_server_group_using_get) | **GET** /applications/{application}/clusters/{account}/{clusterName}/{cloudProvider}/{scope}/serverGroups/target/{target} | Retrieve a server group that matches a target coordinate (e.g., newest, ancestor) relative to a cluster


# **get_cluster_load_balancers_using_get**
> list[object] get_cluster_load_balancers_using_get(application_name, account, cluster_name, type, x_rate_limit_app=x_rate_limit_app)

Retrieve a cluster's loadbalancers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterControllerApi()
application_name = 'application_name_example' # str | applicationName
account = 'account_example' # str | account
cluster_name = 'cluster_name_example' # str | clusterName
type = 'type_example' # str | type
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a cluster's loadbalancers
    api_response = api_instance.get_cluster_load_balancers_using_get(application_name, account, cluster_name, type, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_cluster_load_balancers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| applicationName | 
 **account** | **str**| account | 
 **cluster_name** | **str**| clusterName | 
 **type** | **str**| type | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_using_get**
> dict(str, object) get_clusters_using_get(application, account, cluster_name, x_rate_limit_app=x_rate_limit_app)

Retrieve a cluster's details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterControllerApi()
application = 'application_example' # str | application
account = 'account_example' # str | account
cluster_name = 'cluster_name_example' # str | clusterName
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a cluster's details
    api_response = api_instance.get_clusters_using_get(application, account, cluster_name, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_clusters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **account** | **str**| account | 
 **cluster_name** | **str**| clusterName | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_using_get1**
> list[object] get_clusters_using_get1(application, account, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of clusters for an account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterControllerApi()
application = 'application_example' # str | application
account = 'account_example' # str | account
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of clusters for an account
    api_response = api_instance.get_clusters_using_get1(application, account, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_clusters_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **account** | **str**| account | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_using_get2**
> dict(str, object) get_clusters_using_get2(application, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of cluster names for an application, grouped by account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterControllerApi()
application = 'application_example' # str | application
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of cluster names for an application, grouped by account
    api_response = api_instance.get_clusters_using_get2(application, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_clusters_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scaling_activities_using_get**
> list[object] get_scaling_activities_using_get(application, account, cluster_name, server_group_name, provider=provider, region=region, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of scaling activities for a server group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterControllerApi()
application = 'application_example' # str | application
account = 'account_example' # str | account
cluster_name = 'cluster_name_example' # str | clusterName
server_group_name = 'server_group_name_example' # str | serverGroupName
provider = 'aws' # str | provider (optional) (default to aws)
region = 'region_example' # str | region (optional)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of scaling activities for a server group
    api_response = api_instance.get_scaling_activities_using_get(application, account, cluster_name, server_group_name, provider=provider, region=region, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_scaling_activities_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **account** | **str**| account | 
 **cluster_name** | **str**| clusterName | 
 **server_group_name** | **str**| serverGroupName | 
 **provider** | **str**| provider | [optional] [default to aws]
 **region** | **str**| region | [optional] 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_groups_using_get**
> list[object] get_server_groups_using_get(application, account, cluster_name, server_group_name, x_rate_limit_app=x_rate_limit_app)

Retrieve a server group's details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterControllerApi()
application = 'application_example' # str | application
account = 'account_example' # str | account
cluster_name = 'cluster_name_example' # str | clusterName
server_group_name = 'server_group_name_example' # str | serverGroupName
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a server group's details
    api_response = api_instance.get_server_groups_using_get(application, account, cluster_name, server_group_name, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_server_groups_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **account** | **str**| account | 
 **cluster_name** | **str**| clusterName | 
 **server_group_name** | **str**| serverGroupName | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_groups_using_get1**
> list[object] get_server_groups_using_get1(application, account, cluster_name, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of server groups for a cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterControllerApi()
application = 'application_example' # str | application
account = 'account_example' # str | account
cluster_name = 'cluster_name_example' # str | clusterName
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of server groups for a cluster
    api_response = api_instance.get_server_groups_using_get1(application, account, cluster_name, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_server_groups_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **account** | **str**| account | 
 **cluster_name** | **str**| clusterName | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_server_group_using_get**
> dict(str, object) get_target_server_group_using_get(application, account, cluster_name, cloud_provider, scope, target, only_enabled=only_enabled, validate_oldest=validate_oldest, x_rate_limit_app=x_rate_limit_app)

Retrieve a server group that matches a target coordinate (e.g., newest, ancestor) relative to a cluster

`scope` is either a zone or a region

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterControllerApi()
application = 'application_example' # str | application
account = 'account_example' # str | account
cluster_name = 'cluster_name_example' # str | clusterName
cloud_provider = 'cloud_provider_example' # str | cloudProvider
scope = 'scope_example' # str | scope
target = 'target_example' # str | target
only_enabled = true # bool | onlyEnabled (optional)
validate_oldest = true # bool | validateOldest (optional)
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a server group that matches a target coordinate (e.g., newest, ancestor) relative to a cluster
    api_response = api_instance.get_target_server_group_using_get(application, account, cluster_name, cloud_provider, scope, target, only_enabled=only_enabled, validate_oldest=validate_oldest, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_target_server_group_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **account** | **str**| account | 
 **cluster_name** | **str**| clusterName | 
 **cloud_provider** | **str**| cloudProvider | 
 **scope** | **str**| scope | 
 **target** | **str**| target | 
 **only_enabled** | **bool**| onlyEnabled | [optional] 
 **validate_oldest** | **bool**| validateOldest | [optional] 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

