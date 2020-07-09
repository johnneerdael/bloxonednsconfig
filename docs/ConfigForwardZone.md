# ConfigForwardZone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for zone configuration. | [optional] 
**disabled** | **bool** | Optional. True to disable object. A disabled object is effectively non-existent when generating configuration. | [optional] 
**external_forwarders** | [**list[ConfigForwarder]**](ConfigForwarder.md) | Optional. External DNS servers to forward to. Order is not significant. | [optional] 
**forward_only** | **bool** | Optional. True to only forward. | [optional] 
**fqdn** | **str** | Required. Zone FQDN. The FQDN supplied at creation will be converted to canonical form. Read-only after creation. | 
**hosts** | **list[str]** | The resource identifier. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**internal_forwarders** | **list[str]** | The resource identifier. | [optional] 
**mapped_subnet** | **str** | Read-only. Reverse zone network address in the following format: &lt;ip-address&gt;/&lt;cidr&gt;. Defaults to empty. | [optional] 
**mapping** | **str** | Read-only. Zone mapping type. Allowed values: - forward - ipv4_reverse Defaults to forward. | [optional] 
**nsgs** | **list[str]** | The resource identifier. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol_fqdn** | **str** | Read only. Zone FQDN in punycode. | [optional] 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) |  | [optional] 
**view** | **str** | The resource identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


