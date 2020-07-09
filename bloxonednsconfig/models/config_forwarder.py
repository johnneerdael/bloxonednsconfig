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


class ConfigForwarder(object):
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
        'address': 'str',
        'fqdn': 'str',
        'protocol_fqdn': 'str'
    }

    attribute_map = {
        'address': 'address',
        'fqdn': 'fqdn',
        'protocol_fqdn': 'protocol_fqdn'
    }

    def __init__(self, address=None, fqdn=None, protocol_fqdn=None):  # noqa: E501
        """ConfigForwarder - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._fqdn = None
        self._protocol_fqdn = None
        self.discriminator = None

        self.address = address
        self.fqdn = fqdn
        if protocol_fqdn is not None:
            self.protocol_fqdn = protocol_fqdn

    @property
    def address(self):
        """Gets the address of this ConfigForwarder.  # noqa: E501

        Required. Server IP address.  # noqa: E501

        :return: The address of this ConfigForwarder.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConfigForwarder.

        Required. Server IP address.  # noqa: E501

        :param address: The address of this ConfigForwarder.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def fqdn(self):
        """Gets the fqdn of this ConfigForwarder.  # noqa: E501

        Required. Server FQDN.  # noqa: E501

        :return: The fqdn of this ConfigForwarder.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this ConfigForwarder.

        Required. Server FQDN.  # noqa: E501

        :param fqdn: The fqdn of this ConfigForwarder.  # noqa: E501
        :type: str
        """
        if fqdn is None:
            raise ValueError("Invalid value for `fqdn`, must not be `None`")  # noqa: E501

        self._fqdn = fqdn

    @property
    def protocol_fqdn(self):
        """Gets the protocol_fqdn of this ConfigForwarder.  # noqa: E501

        Read only. Server FQDN in punycode.  # noqa: E501

        :return: The protocol_fqdn of this ConfigForwarder.  # noqa: E501
        :rtype: str
        """
        return self._protocol_fqdn

    @protocol_fqdn.setter
    def protocol_fqdn(self, protocol_fqdn):
        """Sets the protocol_fqdn of this ConfigForwarder.

        Read only. Server FQDN in punycode.  # noqa: E501

        :param protocol_fqdn: The protocol_fqdn of this ConfigForwarder.  # noqa: E501
        :type: str
        """

        self._protocol_fqdn = protocol_fqdn

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
        if issubclass(ConfigForwarder, dict):
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
        if not isinstance(other, ConfigForwarder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
