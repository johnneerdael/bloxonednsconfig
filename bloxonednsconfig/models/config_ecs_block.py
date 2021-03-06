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


class ConfigECSBlock(object):
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
        'ecs_enabled': 'bool',
        'ecs_forwarding': 'bool',
        'ecs_prefix_v4': 'int',
        'ecs_prefix_v6': 'int',
        'ecs_zones': 'list[ConfigECSZone]'
    }

    attribute_map = {
        'ecs_enabled': 'ecs_enabled',
        'ecs_forwarding': 'ecs_forwarding',
        'ecs_prefix_v4': 'ecs_prefix_v4',
        'ecs_prefix_v6': 'ecs_prefix_v6',
        'ecs_zones': 'ecs_zones'
    }

    def __init__(self, ecs_enabled=None, ecs_forwarding=None, ecs_prefix_v4=None, ecs_prefix_v6=None, ecs_zones=None):  # noqa: E501
        """ConfigECSBlock - a model defined in Swagger"""  # noqa: E501

        self._ecs_enabled = None
        self._ecs_forwarding = None
        self._ecs_prefix_v4 = None
        self._ecs_prefix_v6 = None
        self._ecs_zones = None
        self.discriminator = None

        if ecs_enabled is not None:
            self.ecs_enabled = ecs_enabled
        if ecs_forwarding is not None:
            self.ecs_forwarding = ecs_forwarding
        if ecs_prefix_v4 is not None:
            self.ecs_prefix_v4 = ecs_prefix_v4
        if ecs_prefix_v6 is not None:
            self.ecs_prefix_v6 = ecs_prefix_v6
        if ecs_zones is not None:
            self.ecs_zones = ecs_zones

    @property
    def ecs_enabled(self):
        """Gets the ecs_enabled of this ConfigECSBlock.  # noqa: E501

        Optional. Field config for ecs_enabled field.  # noqa: E501

        :return: The ecs_enabled of this ConfigECSBlock.  # noqa: E501
        :rtype: bool
        """
        return self._ecs_enabled

    @ecs_enabled.setter
    def ecs_enabled(self, ecs_enabled):
        """Sets the ecs_enabled of this ConfigECSBlock.

        Optional. Field config for ecs_enabled field.  # noqa: E501

        :param ecs_enabled: The ecs_enabled of this ConfigECSBlock.  # noqa: E501
        :type: bool
        """

        self._ecs_enabled = ecs_enabled

    @property
    def ecs_forwarding(self):
        """Gets the ecs_forwarding of this ConfigECSBlock.  # noqa: E501

        Optional. Field config for ecs_forwarding field.  # noqa: E501

        :return: The ecs_forwarding of this ConfigECSBlock.  # noqa: E501
        :rtype: bool
        """
        return self._ecs_forwarding

    @ecs_forwarding.setter
    def ecs_forwarding(self, ecs_forwarding):
        """Sets the ecs_forwarding of this ConfigECSBlock.

        Optional. Field config for ecs_forwarding field.  # noqa: E501

        :param ecs_forwarding: The ecs_forwarding of this ConfigECSBlock.  # noqa: E501
        :type: bool
        """

        self._ecs_forwarding = ecs_forwarding

    @property
    def ecs_prefix_v4(self):
        """Gets the ecs_prefix_v4 of this ConfigECSBlock.  # noqa: E501

        Optional. Field config for ecs_prefix_v4 field.  # noqa: E501

        :return: The ecs_prefix_v4 of this ConfigECSBlock.  # noqa: E501
        :rtype: int
        """
        return self._ecs_prefix_v4

    @ecs_prefix_v4.setter
    def ecs_prefix_v4(self, ecs_prefix_v4):
        """Sets the ecs_prefix_v4 of this ConfigECSBlock.

        Optional. Field config for ecs_prefix_v4 field.  # noqa: E501

        :param ecs_prefix_v4: The ecs_prefix_v4 of this ConfigECSBlock.  # noqa: E501
        :type: int
        """

        self._ecs_prefix_v4 = ecs_prefix_v4

    @property
    def ecs_prefix_v6(self):
        """Gets the ecs_prefix_v6 of this ConfigECSBlock.  # noqa: E501

        Optional. Field config for ecs_prefix_v6 field.  # noqa: E501

        :return: The ecs_prefix_v6 of this ConfigECSBlock.  # noqa: E501
        :rtype: int
        """
        return self._ecs_prefix_v6

    @ecs_prefix_v6.setter
    def ecs_prefix_v6(self, ecs_prefix_v6):
        """Sets the ecs_prefix_v6 of this ConfigECSBlock.

        Optional. Field config for ecs_prefix_v6 field.  # noqa: E501

        :param ecs_prefix_v6: The ecs_prefix_v6 of this ConfigECSBlock.  # noqa: E501
        :type: int
        """

        self._ecs_prefix_v6 = ecs_prefix_v6

    @property
    def ecs_zones(self):
        """Gets the ecs_zones of this ConfigECSBlock.  # noqa: E501

        Optional. Field config for ecs_zones field from.  # noqa: E501

        :return: The ecs_zones of this ConfigECSBlock.  # noqa: E501
        :rtype: list[ConfigECSZone]
        """
        return self._ecs_zones

    @ecs_zones.setter
    def ecs_zones(self, ecs_zones):
        """Sets the ecs_zones of this ConfigECSBlock.

        Optional. Field config for ecs_zones field from.  # noqa: E501

        :param ecs_zones: The ecs_zones of this ConfigECSBlock.  # noqa: E501
        :type: list[ConfigECSZone]
        """

        self._ecs_zones = ecs_zones

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
        if issubclass(ConfigECSBlock, dict):
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
        if not isinstance(other, ConfigECSBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
