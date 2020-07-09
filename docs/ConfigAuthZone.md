# ConfigAuthZone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for zone configuration. | [optional] 
**disabled** | **bool** | Optional. True to disable object. A disabled object is effectively non-existent when generating configuration. | [optional] 
**external_primaries** | [**list[ConfigExternalPrimary]**](ConfigExternalPrimary.md) | Optional. DNS primaries external to BloxOne DDI. Order is not significant. | [optional] 
**fqdn** | **str** | Required. Zone FQDN. The FQDN supplied at creation will be converted to canonical form. Read-only after creation. | 
**id** | **str** | The resource identifier. | [optional] 
**inheritance_assigned_hosts** | [**list[Inheritance2AssignedHost]**](Inheritance2AssignedHost.md) | Read-only. The list of the inheritance assigned hosts of the object. | [optional] 
**inheritance_sources** | [**ConfigAuthZoneInheritance**](ConfigAuthZoneInheritance.md) |  | [optional] 
**initial_soa_serial** | **int** | On-create-only. SOA serial is allowed to be set when the auth zone is created. | [optional] 
**internal_secondaries** | [**list[ConfigInternalSecondary]**](ConfigInternalSecondary.md) | Optional. BloxOne DDI hosts acting as internal secondaries. Order is not significant. | [optional] 
**mapped_subnet** | **str** | Read-only. Reverse zone network address in the following format: &lt;ip-address&gt;/&lt;cidr&gt;. Defaults to empty. | [optional] 
**mapping** | **str** | Read-only. Zone mapping type. Allowed values: - forward - ipv4_reverse Defaults to forward. | [optional] 
**nsgs** | **list[str]** | The resource identifier. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**primary_type** | **str** | Required. Primary type for an auth zone. Read only after creation. Allowed values: - external: zone data owned by some external to IB nameserver. - cloud: zone data is owned by N* cloud. | 
**protocol_fqdn** | **str** | Read only. Zone FQDN in punycode. | [optional] 
**query_acl** | [**list[ConfigACLItem]**](ConfigACLItem.md) | Optional. Clients must match this ACL to make authoritative queries. Also used for recursive queries if that ACL is unset. Defaults to empty. | [optional] 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) | Tagging specifics. | [optional] 
**transfer_acl** | [**list[ConfigACLItem]**](ConfigACLItem.md) |  | [optional] 
**update_acl** | [**list[ConfigACLItem]**](ConfigACLItem.md) | Optional. Specifies which hosts are allowed to submit Dynamic DNS updates for auth zones of primary_type \&quot;cloud\&quot;. Defaults to empty. | [optional] 
**use_forwarders_for_subzones** | **bool** | Optional. Use default forwarders to resolve queries for subzones. Defaults to true. | [optional] 
**view** | **str** | The resource identifier. | [optional] 
**zone_authority** | [**ConfigZoneAuthority**](ConfigZoneAuthority.md) | Optional. ZoneAuthority. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


