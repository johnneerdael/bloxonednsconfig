# bloxonednsconfig.ConvertDomainNameApi

All URIs are relative to *https://csp.infoblox.com/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_domain_name_convert**](ConvertDomainNameApi.md#convert_domain_name_convert) | **GET** /dns/convert_domain_name/{domain_name} | Convert the object.


# **convert_domain_name_convert**
> ConfigConvertDomainNameResponse convert_domain_name_convert(domain_name)

Convert the object.

Use this method to to convert between Internationalized Domain Name (IDN) and ASCII domain name (Punycode).

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
api_instance = bloxonednsconfig.ConvertDomainNameApi(bloxonednsconfig.ApiClient(configuration))
domain_name = 'domain_name_example' # str | Input domain name in either of IDN or punycode representations.

try:
    # Convert the object.
    api_response = api_instance.convert_domain_name_convert(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDomainNameApi->convert_domain_name_convert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Input domain name in either of IDN or punycode representations. | 

### Return type

[**ConfigConvertDomainNameResponse**](ConfigConvertDomainNameResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

