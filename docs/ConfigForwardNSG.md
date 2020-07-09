# ConfigForwardNSG

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for NSG object. | [optional] 
**external_forwarders** | [**list[ConfigForwarder]**](ConfigForwarder.md) | Optional. External DNS servers to forward to. Order is not significant. | [optional] 
**forwarders_only** | **bool** | Optional. True to only forward. | [optional] 
**hosts** | **list[str]** | The resource identifier. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**internal_forwarders** | **list[str]** | The resource identifier. | [optional] 
**name** | **str** | Required. Name of NSG object. | 
**nsgs** | **list[str]** | The resource identifier. | [optional] 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


