# ConfigHost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_name** | **str** | Read-write. Host FQDN. | [optional] 
**address** | **str** | Read-only. Host&#39;s primary IP Address. | [optional] 
**anycast_addresses** | **list[str]** | Read-only. Anycast address configured to the host. Order is not significant. | [optional] 
**associated_server** | [**ConfigHostAssociatedServer**](ConfigHostAssociatedServer.md) | Host associated server configuration. | [optional] 
**comment** | **str** | Read-only. Host description. | [optional] 
**dfp** | **bool** | Read-only. True if BloxOne DDI DNS and DFP are both active on the host. If so, BloxOne DDI DNS will augment recursive queries and forward them to DFP. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**name** | **str** | Read-only. Host display name. | [optional] 
**ophid** | **str** | Read-only. On-Prem Host ID. | 
**protocol_absolute_name** | **str** | Read-only. Host FQDN in punycode. | [optional] 
**server** | **str** | The resource identifier. | [optional] 
**site_id** | **str** |  | [optional] 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) | Read-only. Host tagging specifics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


