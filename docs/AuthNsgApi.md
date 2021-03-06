# bloxonednsconfig.AuthNsgApi

All URIs are relative to *https://csp.infoblox.com/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_nsg_create**](AuthNsgApi.md#auth_nsg_create) | **POST** /dns/auth_nsg | Create the Auth NSG object.
[**auth_nsg_delete**](AuthNsgApi.md#auth_nsg_delete) | **DELETE** /dns/auth_nsg/{id} | Delete the Auth NSG object.
[**auth_nsg_list**](AuthNsgApi.md#auth_nsg_list) | **GET** /dns/auth_nsg | List Auth NSG objects.
[**auth_nsg_read**](AuthNsgApi.md#auth_nsg_read) | **GET** /dns/auth_nsg/{id} | Read the Auth NSG object.
[**auth_nsg_update**](AuthNsgApi.md#auth_nsg_update) | **PATCH** /dns/auth_nsg/{id} | Update the Auth NSG object.


# **auth_nsg_create**
> ConfigCreateAuthNSGResponse auth_nsg_create(body)

Create the Auth NSG object.

Use this method to create an Auth NSG object. The Auth NSG object represents authoritative nameserver group.

### Example
```python
from __future__ import print_function
import time
import bloxonednsconfig
from bloxonednsconfig.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsconfig.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsconfig.AuthNsgApi(bloxonednsconfig.ApiClient(configuration))
body = bloxonednsconfig.ConfigAuthNSG() # ConfigAuthNSG | 

try:
    # Create the Auth NSG object.
    api_response = api_instance.auth_nsg_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthNsgApi->auth_nsg_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigAuthNSG**](ConfigAuthNSG.md)|  | 

### Return type

[**ConfigCreateAuthNSGResponse**](ConfigCreateAuthNSGResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_nsg_delete**
> auth_nsg_delete(id)

Delete the Auth NSG object.

Use this method to delete an Auth NSG object. The Auth NSG object represents authoritative nameserver group.

### Example
```python
from __future__ import print_function
import time
import bloxonednsconfig
from bloxonednsconfig.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsconfig.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsconfig.AuthNsgApi(bloxonednsconfig.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource

try:
    # Delete the Auth NSG object.
    api_instance.auth_nsg_delete(id)
except ApiException as e:
    print("Exception when calling AuthNsgApi->auth_nsg_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_nsg_list**
> ConfigListAuthNSGResponse auth_nsg_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, tfilter=tfilter, torder_by=torder_by)

List Auth NSG objects.

Use this method to list Auth NSG objects. The Auth NSG object represents authoritative nameserver group.

### Example
```python
from __future__ import print_function
import time
import bloxonednsconfig
from bloxonednsconfig.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsconfig.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsconfig.AuthNsgApi(bloxonednsconfig.ApiClient(configuration))
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)
torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)

try:
    # List Auth NSG objects.
    api_response = api_instance.auth_nsg_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, tfilter=tfilter, torder_by=torder_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthNsgApi->auth_nsg_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 

### Return type

[**ConfigListAuthNSGResponse**](ConfigListAuthNSGResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_nsg_read**
> ConfigReadAuthNSGResponse auth_nsg_read(id, fields=fields)

Read the Auth NSG object.

Use this method to read an Auth NSG object. The Auth NSG object represents authoritative nameserver group.

### Example
```python
from __future__ import print_function
import time
import bloxonednsconfig
from bloxonednsconfig.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsconfig.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsconfig.AuthNsgApi(bloxonednsconfig.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the Auth NSG object.
    api_response = api_instance.auth_nsg_read(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthNsgApi->auth_nsg_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**ConfigReadAuthNSGResponse**](ConfigReadAuthNSGResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_nsg_update**
> ConfigUpdateAuthNSGResponse auth_nsg_update(id, body)

Update the Auth NSG object.

Use this method to update an Auth NSG object. The Auth NSG object represents authoritative nameserver group.

### Example
```python
from __future__ import print_function
import time
import bloxonednsconfig
from bloxonednsconfig.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsconfig.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsconfig.AuthNsgApi(bloxonednsconfig.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
body = bloxonednsconfig.ConfigAuthNSG() # ConfigAuthNSG | 

try:
    # Update the Auth NSG object.
    api_response = api_instance.auth_nsg_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthNsgApi->auth_nsg_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**ConfigAuthNSG**](ConfigAuthNSG.md)|  | 

### Return type

[**ConfigUpdateAuthNSGResponse**](ConfigUpdateAuthNSGResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

