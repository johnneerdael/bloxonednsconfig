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


class ConfigInheritedZoneAuthority(object):
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
        'default_ttl': 'Inheritance2InheritedUInt32',
        'expire': 'Inheritance2InheritedUInt32',
        'negative_ttl': 'Inheritance2InheritedUInt32',
        'protocol_rname': 'Inheritance2InheritedString',
        'refresh': 'Inheritance2InheritedUInt32',
        'retry': 'Inheritance2InheritedUInt32',
        'rname': 'Inheritance2InheritedString'
    }

    attribute_map = {
        'default_ttl': 'default_ttl',
        'expire': 'expire',
        'negative_ttl': 'negative_ttl',
        'protocol_rname': 'protocol_rname',
        'refresh': 'refresh',
        'retry': 'retry',
        'rname': 'rname'
    }

    def __init__(self, default_ttl=None, expire=None, negative_ttl=None, protocol_rname=None, refresh=None, retry=None, rname=None):  # noqa: E501
        """ConfigInheritedZoneAuthority - a model defined in Swagger"""  # noqa: E501

        self._default_ttl = None
        self._expire = None
        self._negative_ttl = None
        self._protocol_rname = None
        self._refresh = None
        self._retry = None
        self._rname = None
        self.discriminator = None

        if default_ttl is not None:
            self.default_ttl = default_ttl
        if expire is not None:
            self.expire = expire
        if negative_ttl is not None:
            self.negative_ttl = negative_ttl
        if protocol_rname is not None:
            self.protocol_rname = protocol_rname
        if refresh is not None:
            self.refresh = refresh
        if retry is not None:
            self.retry = retry
        if rname is not None:
            self.rname = rname

    @property
    def default_ttl(self):
        """Gets the default_ttl of this ConfigInheritedZoneAuthority.  # noqa: E501

        Optional. Field config for default_ttl field from [ZoneAuthority] object.  # noqa: E501

        :return: The default_ttl of this ConfigInheritedZoneAuthority.  # noqa: E501
        :rtype: Inheritance2InheritedUInt32
        """
        return self._default_ttl

    @default_ttl.setter
    def default_ttl(self, default_ttl):
        """Sets the default_ttl of this ConfigInheritedZoneAuthority.

        Optional. Field config for default_ttl field from [ZoneAuthority] object.  # noqa: E501

        :param default_ttl: The default_ttl of this ConfigInheritedZoneAuthority.  # noqa: E501
        :type: Inheritance2InheritedUInt32
        """

        self._default_ttl = default_ttl

    @property
    def expire(self):
        """Gets the expire of this ConfigInheritedZoneAuthority.  # noqa: E501

        Optional. Field config for expire field from [ZoneAuthority] object.  # noqa: E501

        :return: The expire of this ConfigInheritedZoneAuthority.  # noqa: E501
        :rtype: Inheritance2InheritedUInt32
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """Sets the expire of this ConfigInheritedZoneAuthority.

        Optional. Field config for expire field from [ZoneAuthority] object.  # noqa: E501

        :param expire: The expire of this ConfigInheritedZoneAuthority.  # noqa: E501
        :type: Inheritance2InheritedUInt32
        """

        self._expire = expire

    @property
    def negative_ttl(self):
        """Gets the negative_ttl of this ConfigInheritedZoneAuthority.  # noqa: E501

        Optional. Field config for negative_ttl field from [ZoneAuthority] object.  # noqa: E501

        :return: The negative_ttl of this ConfigInheritedZoneAuthority.  # noqa: E501
        :rtype: Inheritance2InheritedUInt32
        """
        return self._negative_ttl

    @negative_ttl.setter
    def negative_ttl(self, negative_ttl):
        """Sets the negative_ttl of this ConfigInheritedZoneAuthority.

        Optional. Field config for negative_ttl field from [ZoneAuthority] object.  # noqa: E501

        :param negative_ttl: The negative_ttl of this ConfigInheritedZoneAuthority.  # noqa: E501
        :type: Inheritance2InheritedUInt32
        """

        self._negative_ttl = negative_ttl

    @property
    def protocol_rname(self):
        """Gets the protocol_rname of this ConfigInheritedZoneAuthority.  # noqa: E501

        Optional. Field config for protocol_rname field from [ZoneAuthority] object.  # noqa: E501

        :return: The protocol_rname of this ConfigInheritedZoneAuthority.  # noqa: E501
        :rtype: Inheritance2InheritedString
        """
        return self._protocol_rname

    @protocol_rname.setter
    def protocol_rname(self, protocol_rname):
        """Sets the protocol_rname of this ConfigInheritedZoneAuthority.

        Optional. Field config for protocol_rname field from [ZoneAuthority] object.  # noqa: E501

        :param protocol_rname: The protocol_rname of this ConfigInheritedZoneAuthority.  # noqa: E501
        :type: Inheritance2InheritedString
        """

        self._protocol_rname = protocol_rname

    @property
    def refresh(self):
        """Gets the refresh of this ConfigInheritedZoneAuthority.  # noqa: E501

        Optional. Field config for refresh field from [ZoneAuthority] object.  # noqa: E501

        :return: The refresh of this ConfigInheritedZoneAuthority.  # noqa: E501
        :rtype: Inheritance2InheritedUInt32
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this ConfigInheritedZoneAuthority.

        Optional. Field config for refresh field from [ZoneAuthority] object.  # noqa: E501

        :param refresh: The refresh of this ConfigInheritedZoneAuthority.  # noqa: E501
        :type: Inheritance2InheritedUInt32
        """

        self._refresh = refresh

    @property
    def retry(self):
        """Gets the retry of this ConfigInheritedZoneAuthority.  # noqa: E501

        Optional. Field config for retry field from [ZoneAuthority] object.  # noqa: E501

        :return: The retry of this ConfigInheritedZoneAuthority.  # noqa: E501
        :rtype: Inheritance2InheritedUInt32
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this ConfigInheritedZoneAuthority.

        Optional. Field config for retry field from [ZoneAuthority] object.  # noqa: E501

        :param retry: The retry of this ConfigInheritedZoneAuthority.  # noqa: E501
        :type: Inheritance2InheritedUInt32
        """

        self._retry = retry

    @property
    def rname(self):
        """Gets the rname of this ConfigInheritedZoneAuthority.  # noqa: E501

        Optional. Field config for rname field from [ZoneAuthority] object.  # noqa: E501

        :return: The rname of this ConfigInheritedZoneAuthority.  # noqa: E501
        :rtype: Inheritance2InheritedString
        """
        return self._rname

    @rname.setter
    def rname(self, rname):
        """Sets the rname of this ConfigInheritedZoneAuthority.

        Optional. Field config for rname field from [ZoneAuthority] object.  # noqa: E501

        :param rname: The rname of this ConfigInheritedZoneAuthority.  # noqa: E501
        :type: Inheritance2InheritedString
        """

        self._rname = rname

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
        if issubclass(ConfigInheritedZoneAuthority, dict):
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
        if not isinstance(other, ConfigInheritedZoneAuthority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
