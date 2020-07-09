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


class ConfigDNSSECValidationBlock(object):
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
        'dnssec_enable_validation': 'bool',
        'dnssec_enabled': 'bool',
        'dnssec_trust_anchors': 'list[ConfigTrustAnchor]',
        'dnssec_validate_expiry': 'bool'
    }

    attribute_map = {
        'dnssec_enable_validation': 'dnssec_enable_validation',
        'dnssec_enabled': 'dnssec_enabled',
        'dnssec_trust_anchors': 'dnssec_trust_anchors',
        'dnssec_validate_expiry': 'dnssec_validate_expiry'
    }

    def __init__(self, dnssec_enable_validation=None, dnssec_enabled=None, dnssec_trust_anchors=None, dnssec_validate_expiry=None):  # noqa: E501
        """ConfigDNSSECValidationBlock - a model defined in Swagger"""  # noqa: E501

        self._dnssec_enable_validation = None
        self._dnssec_enabled = None
        self._dnssec_trust_anchors = None
        self._dnssec_validate_expiry = None
        self.discriminator = None

        if dnssec_enable_validation is not None:
            self.dnssec_enable_validation = dnssec_enable_validation
        if dnssec_enabled is not None:
            self.dnssec_enabled = dnssec_enabled
        if dnssec_trust_anchors is not None:
            self.dnssec_trust_anchors = dnssec_trust_anchors
        if dnssec_validate_expiry is not None:
            self.dnssec_validate_expiry = dnssec_validate_expiry

    @property
    def dnssec_enable_validation(self):
        """Gets the dnssec_enable_validation of this ConfigDNSSECValidationBlock.  # noqa: E501

        Optional. Field config for dnssec_enable_validation field.  # noqa: E501

        :return: The dnssec_enable_validation of this ConfigDNSSECValidationBlock.  # noqa: E501
        :rtype: bool
        """
        return self._dnssec_enable_validation

    @dnssec_enable_validation.setter
    def dnssec_enable_validation(self, dnssec_enable_validation):
        """Sets the dnssec_enable_validation of this ConfigDNSSECValidationBlock.

        Optional. Field config for dnssec_enable_validation field.  # noqa: E501

        :param dnssec_enable_validation: The dnssec_enable_validation of this ConfigDNSSECValidationBlock.  # noqa: E501
        :type: bool
        """

        self._dnssec_enable_validation = dnssec_enable_validation

    @property
    def dnssec_enabled(self):
        """Gets the dnssec_enabled of this ConfigDNSSECValidationBlock.  # noqa: E501

        Optional. Field config for dnssec_enabled field.  # noqa: E501

        :return: The dnssec_enabled of this ConfigDNSSECValidationBlock.  # noqa: E501
        :rtype: bool
        """
        return self._dnssec_enabled

    @dnssec_enabled.setter
    def dnssec_enabled(self, dnssec_enabled):
        """Sets the dnssec_enabled of this ConfigDNSSECValidationBlock.

        Optional. Field config for dnssec_enabled field.  # noqa: E501

        :param dnssec_enabled: The dnssec_enabled of this ConfigDNSSECValidationBlock.  # noqa: E501
        :type: bool
        """

        self._dnssec_enabled = dnssec_enabled

    @property
    def dnssec_trust_anchors(self):
        """Gets the dnssec_trust_anchors of this ConfigDNSSECValidationBlock.  # noqa: E501

        Optional. Field config for dnssec_trust_anchors field.  # noqa: E501

        :return: The dnssec_trust_anchors of this ConfigDNSSECValidationBlock.  # noqa: E501
        :rtype: list[ConfigTrustAnchor]
        """
        return self._dnssec_trust_anchors

    @dnssec_trust_anchors.setter
    def dnssec_trust_anchors(self, dnssec_trust_anchors):
        """Sets the dnssec_trust_anchors of this ConfigDNSSECValidationBlock.

        Optional. Field config for dnssec_trust_anchors field.  # noqa: E501

        :param dnssec_trust_anchors: The dnssec_trust_anchors of this ConfigDNSSECValidationBlock.  # noqa: E501
        :type: list[ConfigTrustAnchor]
        """

        self._dnssec_trust_anchors = dnssec_trust_anchors

    @property
    def dnssec_validate_expiry(self):
        """Gets the dnssec_validate_expiry of this ConfigDNSSECValidationBlock.  # noqa: E501

        Optional. Field config for dnssec_validate_expiry field.  # noqa: E501

        :return: The dnssec_validate_expiry of this ConfigDNSSECValidationBlock.  # noqa: E501
        :rtype: bool
        """
        return self._dnssec_validate_expiry

    @dnssec_validate_expiry.setter
    def dnssec_validate_expiry(self, dnssec_validate_expiry):
        """Sets the dnssec_validate_expiry of this ConfigDNSSECValidationBlock.

        Optional. Field config for dnssec_validate_expiry field.  # noqa: E501

        :param dnssec_validate_expiry: The dnssec_validate_expiry of this ConfigDNSSECValidationBlock.  # noqa: E501
        :type: bool
        """

        self._dnssec_validate_expiry = dnssec_validate_expiry

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
        if issubclass(ConfigDNSSECValidationBlock, dict):
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
        if not isinstance(other, ConfigDNSSECValidationBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
