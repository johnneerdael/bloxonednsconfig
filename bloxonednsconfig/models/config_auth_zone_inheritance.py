# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ConfigAuthZoneInheritance(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'query_acl': 'ConfigInheritedACLItems',
        'transfer_acl': 'ConfigInheritedACLItems',
        'update_acl': 'ConfigInheritedACLItems',
        'use_forwarders_for_subzones': 'Inheritance2InheritedBool',
        'zone_authority': 'ConfigInheritedZoneAuthority'
    }

    attribute_map = {
        'query_acl': 'query_acl',
        'transfer_acl': 'transfer_acl',
        'update_acl': 'update_acl',
        'use_forwarders_for_subzones': 'use_forwarders_for_subzones',
        'zone_authority': 'zone_authority'
    }

    def __init__(self, query_acl=None, transfer_acl=None, update_acl=None, use_forwarders_for_subzones=None, zone_authority=None):  # noqa: E501
        """ConfigAuthZoneInheritance - a model defined in Swagger"""  # noqa: E501

        self._query_acl = None
        self._transfer_acl = None
        self._update_acl = None
        self._use_forwarders_for_subzones = None
        self._zone_authority = None
        self.discriminator = None

        if query_acl is not None:
            self.query_acl = query_acl
        if transfer_acl is not None:
            self.transfer_acl = transfer_acl
        if update_acl is not None:
            self.update_acl = update_acl
        if use_forwarders_for_subzones is not None:
            self.use_forwarders_for_subzones = use_forwarders_for_subzones
        if zone_authority is not None:
            self.zone_authority = zone_authority

    @property
    def query_acl(self):
        """Gets the query_acl of this ConfigAuthZoneInheritance.  # noqa: E501

        Optional. Field config for query_acl field from [AuthZone] object.  # noqa: E501

        :return: The query_acl of this ConfigAuthZoneInheritance.  # noqa: E501
        :rtype: ConfigInheritedACLItems
        """
        return self._query_acl

    @query_acl.setter
    def query_acl(self, query_acl):
        """Sets the query_acl of this ConfigAuthZoneInheritance.

        Optional. Field config for query_acl field from [AuthZone] object.  # noqa: E501

        :param query_acl: The query_acl of this ConfigAuthZoneInheritance.  # noqa: E501
        :type: ConfigInheritedACLItems
        """

        self._query_acl = query_acl

    @property
    def transfer_acl(self):
        """Gets the transfer_acl of this ConfigAuthZoneInheritance.  # noqa: E501

        Optional. Field config for transfer_acl field from [AuthZone] object.  # noqa: E501

        :return: The transfer_acl of this ConfigAuthZoneInheritance.  # noqa: E501
        :rtype: ConfigInheritedACLItems
        """
        return self._transfer_acl

    @transfer_acl.setter
    def transfer_acl(self, transfer_acl):
        """Sets the transfer_acl of this ConfigAuthZoneInheritance.

        Optional. Field config for transfer_acl field from [AuthZone] object.  # noqa: E501

        :param transfer_acl: The transfer_acl of this ConfigAuthZoneInheritance.  # noqa: E501
        :type: ConfigInheritedACLItems
        """

        self._transfer_acl = transfer_acl

    @property
    def update_acl(self):
        """Gets the update_acl of this ConfigAuthZoneInheritance.  # noqa: E501

        Optional. Field config for update_acl field from [AuthZone] object.  # noqa: E501

        :return: The update_acl of this ConfigAuthZoneInheritance.  # noqa: E501
        :rtype: ConfigInheritedACLItems
        """
        return self._update_acl

    @update_acl.setter
    def update_acl(self, update_acl):
        """Sets the update_acl of this ConfigAuthZoneInheritance.

        Optional. Field config for update_acl field from [AuthZone] object.  # noqa: E501

        :param update_acl: The update_acl of this ConfigAuthZoneInheritance.  # noqa: E501
        :type: ConfigInheritedACLItems
        """

        self._update_acl = update_acl

    @property
    def use_forwarders_for_subzones(self):
        """Gets the use_forwarders_for_subzones of this ConfigAuthZoneInheritance.  # noqa: E501

        Optional. Field config for use_forwarders_for_subzones field from [AuthZone] object.  # noqa: E501

        :return: The use_forwarders_for_subzones of this ConfigAuthZoneInheritance.  # noqa: E501
        :rtype: Inheritance2InheritedBool
        """
        return self._use_forwarders_for_subzones

    @use_forwarders_for_subzones.setter
    def use_forwarders_for_subzones(self, use_forwarders_for_subzones):
        """Sets the use_forwarders_for_subzones of this ConfigAuthZoneInheritance.

        Optional. Field config for use_forwarders_for_subzones field from [AuthZone] object.  # noqa: E501

        :param use_forwarders_for_subzones: The use_forwarders_for_subzones of this ConfigAuthZoneInheritance.  # noqa: E501
        :type: Inheritance2InheritedBool
        """

        self._use_forwarders_for_subzones = use_forwarders_for_subzones

    @property
    def zone_authority(self):
        """Gets the zone_authority of this ConfigAuthZoneInheritance.  # noqa: E501

        Optional. Field config for zone_authority field from [AuthZone] object.  # noqa: E501

        :return: The zone_authority of this ConfigAuthZoneInheritance.  # noqa: E501
        :rtype: ConfigInheritedZoneAuthority
        """
        return self._zone_authority

    @zone_authority.setter
    def zone_authority(self, zone_authority):
        """Sets the zone_authority of this ConfigAuthZoneInheritance.

        Optional. Field config for zone_authority field from [AuthZone] object.  # noqa: E501

        :param zone_authority: The zone_authority of this ConfigAuthZoneInheritance.  # noqa: E501
        :type: ConfigInheritedZoneAuthority
        """

        self._zone_authority = zone_authority

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConfigAuthZoneInheritance, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigAuthZoneInheritance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other