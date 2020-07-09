# ConfigGlobal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_root_ns** | [**list[ConfigRootNS]**](ConfigRootNS.md) | Optional. List of custom root nameservers. The order does not matter. Error if empty while custom_root_ns_enabled is true. Error if there are duplicate items in the list. Defaults to empty. | [optional] 
**custom_root_ns_enabled** | **bool** | Optional. True to use custom root nameservers instead of the default ones. The custom_root_ns is validated when enabled. Defaults to false. | [optional] 
**dnssec_enable_validation** | **bool** | Optional. True to perform DNSSEC validation. Ignored if dnssec_enabled is false. Defaults to true. | [optional] 
**dnssec_enabled** | **bool** | Optional. Master toggle for all DNSSEC processing. Other dnssec_* configuration is unused if this is disabled. Defaults to true. | [optional] 
**dnssec_root_keys** | [**list[ConfigTrustAnchor]**](ConfigTrustAnchor.md) | Read-only. DNSSEC root keys. The root keys are not configurable. A default list is provided by cloud management and included here for config generation. | [optional] 
**dnssec_trust_anchors** | [**list[ConfigTrustAnchor]**](ConfigTrustAnchor.md) | Optional. DNSSEC trust anchors. Error if there are list items with duplicate (zone, sep, algorithm) combinations. Defaults to empty. | [optional] 
**dnssec_validate_expiry** | **bool** | Optional. True to reject expired DNSSEC keys. Ignored if either dnssec_enabled or dnssec_enable_validation is false. Defaults to true. | [optional] 
**ecs_enabled** | **bool** | Optional. True to enable EDNS client subnet for recursive queries. Other ecs_* fields are ignored if this field is not enabled. Defaults to false. | [optional] 
**ecs_forwarding** | **bool** | Optional. True to enable ECS options in outbound queries. This functionality has additional overhead so it is disabled by default. Defaults to false. | [optional] 
**ecs_prefix_v4** | **int** | Optional. Maximum scope length for v4 ECS. Unsigned integer, min 1 max 24. Defaults to 24. | [optional] 
**ecs_prefix_v6** | **int** | Optional. Maximum scope length for v6 ECS. Unsigned integer, min 1 max 56. Defaults to 56. | [optional] 
**ecs_zones** | [**list[ConfigECSZone]**](ConfigECSZone.md) | Optional. List of zones where ECS queries may be sent. Error if empty while ecs_enabled is true. Error if there are duplicate FQDNs in the list. Defaults to empty. | [optional] 
**forwarders** | [**list[ConfigForwarder]**](ConfigForwarder.md) | Optional. List of forwarders. Error if empty while forwarders_only is true. Error if there are items in the list with duplicate addresses. Defaults to empty. | [optional] 
**forwarders_only** | **bool** | Optional. True to only forward. Defaults to false. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**lame_ttl** | **int** | Optional. Seconds to cache lame server indications. Setting this to zero disables caching, which is not recommended. Unsigned integer, min 0 max 3600 (1h). Defaults to 600. | [optional] 
**log_query_response** | **bool** | Optional. Control DNS query/response logging functionality. Defaults to true. | [optional] 
**match_recursive_only** | **bool** | Optional. If true only recursive queries from matching clients access the view. Defaults to false. | [optional] 
**max_cache_ttl** | **int** | Optional. Seconds to cache positive responses. Unsigned integer, min 1 max 604800 (7d). Defaults to 604800 (7d). | [optional] 
**max_negative_ttl** | **int** | Optional. Seconds to cache negative responses. Unsigned integer, min 1 max 604800 (7d). Defaults to 10800 (3h). | [optional] 
**minimal_responses** | **bool** | Optional. When enabled, the DNS server will only add records to the authority and additional data sections when they are required. Defaults to false. | [optional] 
**query_acl** | [**list[ConfigACLItem]**](ConfigACLItem.md) | Optional. Clients must match this ACL to make authoritative queries. Also used for recursive queries if that ACL is unset. Defaults to empty. | [optional] 
**query_port** | **int** | Optional. Source port for outbound DNS queries. When set to zero the port is unspecified and the implementation may randomize it using any available ports. Defaults to 0. | [optional] 
**recursion_acl** | [**list[ConfigACLItem]**](ConfigACLItem.md) | Optional. Clients must match this ACL to make recursive  queries. If this ACL is empty, then the query_acl will be used instead. Defaults to empty. | [optional] 
**recursion_enabled** | **bool** | Optional. True to allow recursive DNS queries. Defaults to true. | [optional] 
**resolver_query_timeout** | **int** | Optional. Seconds before a recursive query times out. Unsigned integer, min 1 max 30. Defaults to 30. | [optional] 
**secondary_axfr_query_limit** | **int** | Optional. Maximum concurrent inbound AXFRs. When set to zero a host-dependent default will be used. Defaults to 0. | [optional] 
**secondary_soa_query_limit** | **int** | Optional. Maximum concurrent outbound SOA queries. When set to zero a host-dependent default will be used. Defaults to 0. | [optional] 
**transfer_acl** | [**list[ConfigACLItem]**](ConfigACLItem.md) | Optional. Clients must match this ACL to receive zone transfers. Defaults to \&quot;deny any\&quot;. | [optional] 
**update_acl** | [**list[ConfigACLItem]**](ConfigACLItem.md) | Optional. Specifies which hosts are allowed to issue Dynamic DNS updates for auth zones of primary_type \&quot;cloud\&quot;. Defaults to empty. | [optional] 
**use_forwarders_for_subzones** | **bool** | Optional. Use default forwarders to resolve queries for subzones. Defaults to true. | [optional] 
**zone_authority** | [**ConfigZoneAuthority**](ConfigZoneAuthority.md) | Optional. ZoneAuthority. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


