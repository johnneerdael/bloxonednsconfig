# bloxonednsconfig.ConvertRnameApi

All URIs are relative to *https://csp.infoblox.com/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_rname_convert_r_name**](ConvertRnameApi.md#convert_rname_convert_r_name) | **GET** /dns/convert_rname/{email_address} | Convert the object.


# **convert_rname_convert_r_name**
> ConfigConvertRNameResponse convert_rname_convert_r_name(email_address)

Convert the object.

Use this method to to convert email address to the master file RNAME format.

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
api_instance = bloxonednsconfig.ConvertRnameApi(bloxonednsconfig.ApiClient(configuration))
email_address = 'email_address_example' # str | Input email address.

try:
    # Convert the object.
    api_response = api_instance.convert_rname_convert_r_name(email_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertRnameApi->convert_rname_convert_r_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| Input email address. | 

### Return type

[**ConfigConvertRNameResponse**](ConfigConvertRNameResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

