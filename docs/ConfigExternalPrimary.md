# ConfigExternalPrimary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Optional. Required only if type is \&quot;server\&quot;. IP Address of nameserver. | [optional] 
**fqdn** | **str** | Optional. Required only if type is \&quot;server\&quot;. FQDN of nameserver. | [optional] 
**nsg** | **str** | The resource identifier. | [optional] 
**protocol_fqdn** | **str** | Read only. TSIG key&#39;s DNS name (FQDN) in punycode. | [optional] 
**protocol_tsig_key_name** | **str** | Read only. FQDN of nameserver in punycode. | [optional] 
**tsig_enabled** | **bool** | Optional. If enabled, secondaries will use the configured TSIG key when requesting a zone transfer from this primary. | [optional] 
**tsig_key_algo** | **str** | Optional. TSIG key algorithm. Allowed values: - hmac_md5 - hmac_sha1 - hmac_sha224 - hmac_sha256 - hmac_sha384 - hmac_sha512 Defaults to hmac_sha256. | [optional] 
**tsig_key_data** | **str** | Optional. TSIG key data. Error if empty while tsig_enabled is true. | [optional] 
**tsig_key_name** | **str** | Optional. TSIG key&#39;s DNS name (FQDN). Error if empty while tsig_enabled is true. | [optional] 
**type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


