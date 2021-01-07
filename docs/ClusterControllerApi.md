# spinnaker_client.ClusterControllerApi

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
> list[object] get_cluster_load_balancers_using_get(account, application_name, cluster_name, type, x_rate_limit_app=x_rate_limit_app)

Retrieve a cluster's loadbalancers

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ClusterControllerApi()
account = 'account_example' # str | account
application_name = 'application_name_example' # str | applicationName
cluster_name = 'cluster_name_example' # str | clusterName
type = 'type_example' # str | type
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a cluster's loadbalancers
    api_response = api_instance.get_cluster_load_balancers_using_get(account, application_name, cluster_name, type, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_cluster_load_balancers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application_name** | **str**| applicationName | 
 **cluster_name** | **str**| clusterName | 
 **type** | **str**| type | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_using_get**
> dict(str, object) get_clusters_using_get(account, application, cluster_name, x_rate_limit_app=x_rate_limit_app)

Retrieve a cluster's details

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ClusterControllerApi()
account = 'account_example' # str | account
application = 'application_example' # str | application
cluster_name = 'cluster_name_example' # str | clusterName
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a cluster's details
    api_response = api_instance.get_clusters_using_get(account, application, cluster_name, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_clusters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application** | **str**| application | 
 **cluster_name** | **str**| clusterName | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_using_get1**
> list[object] get_clusters_using_get1(account, application, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of clusters for an account

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ClusterControllerApi()
account = 'account_example' # str | account
application = 'application_example' # str | application
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of clusters for an account
    api_response = api_instance.get_clusters_using_get1(account, application, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_clusters_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application** | **str**| application | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_using_get2**
> dict(str, object) get_clusters_using_get2(application, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of cluster names for an application, grouped by account

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ClusterControllerApi()
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

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scaling_activities_using_get**
> list[object] get_scaling_activities_using_get(account, application, cluster_name, server_group_name, x_rate_limit_app=x_rate_limit_app, provider=provider, region=region)

Retrieve a list of scaling activities for a server group

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ClusterControllerApi()
account = 'account_example' # str | account
application = 'application_example' # str | application
cluster_name = 'cluster_name_example' # str | clusterName
server_group_name = 'server_group_name_example' # str | serverGroupName
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
provider = 'aws' # str | provider (optional) (default to aws)
region = 'region_example' # str | region (optional)

try:
    # Retrieve a list of scaling activities for a server group
    api_response = api_instance.get_scaling_activities_using_get(account, application, cluster_name, server_group_name, x_rate_limit_app=x_rate_limit_app, provider=provider, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_scaling_activities_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application** | **str**| application | 
 **cluster_name** | **str**| clusterName | 
 **server_group_name** | **str**| serverGroupName | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **provider** | **str**| provider | [optional] [default to aws]
 **region** | **str**| region | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_groups_using_get**
> list[object] get_server_groups_using_get(account, application, cluster_name, server_group_name, x_rate_limit_app=x_rate_limit_app)

Retrieve a server group's details

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ClusterControllerApi()
account = 'account_example' # str | account
application = 'application_example' # str | application
cluster_name = 'cluster_name_example' # str | clusterName
server_group_name = 'server_group_name_example' # str | serverGroupName
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a server group's details
    api_response = api_instance.get_server_groups_using_get(account, application, cluster_name, server_group_name, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_server_groups_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application** | **str**| application | 
 **cluster_name** | **str**| clusterName | 
 **server_group_name** | **str**| serverGroupName | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_groups_using_get1**
> list[object] get_server_groups_using_get1(account, application, cluster_name, x_rate_limit_app=x_rate_limit_app)

Retrieve a list of server groups for a cluster

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ClusterControllerApi()
account = 'account_example' # str | account
application = 'application_example' # str | application
cluster_name = 'cluster_name_example' # str | clusterName
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)

try:
    # Retrieve a list of server groups for a cluster
    api_response = api_instance.get_server_groups_using_get1(account, application, cluster_name, x_rate_limit_app=x_rate_limit_app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_server_groups_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application** | **str**| application | 
 **cluster_name** | **str**| clusterName | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_server_group_using_get**
> dict(str, object) get_target_server_group_using_get(account, application, cloud_provider, cluster_name, scope, target, x_rate_limit_app=x_rate_limit_app, only_enabled=only_enabled, validate_oldest=validate_oldest)

Retrieve a server group that matches a target coordinate (e.g., newest, ancestor) relative to a cluster

`scope` is either a zone or a region

### Example
```python
from __future__ import print_function
import time
import spinnaker_client
from spinnaker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = spinnaker_client.ClusterControllerApi()
account = 'account_example' # str | account
application = 'application_example' # str | application
cloud_provider = 'cloud_provider_example' # str | cloudProvider
cluster_name = 'cluster_name_example' # str | clusterName
scope = 'scope_example' # str | scope
target = 'target_example' # str | target
x_rate_limit_app = 'x_rate_limit_app_example' # str | X-RateLimit-App (optional)
only_enabled = true # bool | onlyEnabled (optional)
validate_oldest = true # bool | validateOldest (optional)

try:
    # Retrieve a server group that matches a target coordinate (e.g., newest, ancestor) relative to a cluster
    api_response = api_instance.get_target_server_group_using_get(account, application, cloud_provider, cluster_name, scope, target, x_rate_limit_app=x_rate_limit_app, only_enabled=only_enabled, validate_oldest=validate_oldest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterControllerApi->get_target_server_group_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| account | 
 **application** | **str**| application | 
 **cloud_provider** | **str**| cloudProvider | 
 **cluster_name** | **str**| clusterName | 
 **scope** | **str**| scope | 
 **target** | **str**| target | 
 **x_rate_limit_app** | **str**| X-RateLimit-App | [optional] 
 **only_enabled** | **bool**| onlyEnabled | [optional] 
 **validate_oldest** | **bool**| validateOldest | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

