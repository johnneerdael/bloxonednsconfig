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


class ConfigForwardNSG(object):
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
        'comment': 'str',
        'external_forwarders': 'list[ConfigForwarder]',
        'forwarders_only': 'bool',
        'hosts': 'list[str]',
        'id': 'str',
        'internal_forwarders': 'list[str]',
        'name': 'str',
        'nsgs': 'list[str]',
        'tags': 'TypesJSONValue'
    }

    attribute_map = {
        'comment': 'comment',
        'external_forwarders': 'external_forwarders',
        'forwarders_only': 'forwarders_only',
        'hosts': 'hosts',
        'id': 'id',
        'internal_forwarders': 'internal_forwarders',
        'name': 'name',
        'nsgs': 'nsgs',
        'tags': 'tags'
    }

    def __init__(self, comment=None, external_forwarders=None, forwarders_only=None, hosts=None, id=None, internal_forwarders=None, name=None, nsgs=None, tags=None):  # noqa: E501
        """ConfigForwardNSG - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._external_forwarders = None
        self._forwarders_only = None
        self._hosts = None
        self._id = None
        self._internal_forwarders = None
        self._name = None
        self._nsgs = None
        self._tags = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if external_forwarders is not None:
            self.external_forwarders = external_forwarders
        if forwarders_only is not None:
            self.forwarders_only = forwarders_only
        if hosts is not None:
            self.hosts = hosts
        if id is not None:
            self.id = id
        if internal_forwarders is not None:
            self.internal_forwarders = internal_forwarders
        self.name = name
        if nsgs is not None:
            self.nsgs = nsgs
        if tags is not None:
            self.tags = tags

    @property
    def comment(self):
        """Gets the comment of this ConfigForwardNSG.  # noqa: E501

        Optional. Comment for NSG object.  # noqa: E501

        :return: The comment of this ConfigForwardNSG.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ConfigForwardNSG.

        Optional. Comment for NSG object.  # noqa: E501

        :param comment: The comment of this ConfigForwardNSG.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def external_forwarders(self):
        """Gets the external_forwarders of this ConfigForwardNSG.  # noqa: E501

        Optional. External DNS servers to forward to. Order is not significant.  # noqa: E501

        :return: The external_forwarders of this ConfigForwardNSG.  # noqa: E501
        :rtype: list[ConfigForwarder]
        """
        return self._external_forwarders

    @external_forwarders.setter
    def external_forwarders(self, external_forwarders):
        """Sets the external_forwarders of this ConfigForwardNSG.

        Optional. External DNS servers to forward to. Order is not significant.  # noqa: E501

        :param external_forwarders: The external_forwarders of this ConfigForwardNSG.  # noqa: E501
        :type: list[ConfigForwarder]
        """

        self._external_forwarders = external_forwarders

    @property
    def forwarders_only(self):
        """Gets the forwarders_only of this ConfigForwardNSG.  # noqa: E501

        Optional. True to only forward.  # noqa: E501

        :return: The forwarders_only of this ConfigForwardNSG.  # noqa: E501
        :rtype: bool
        """
        return self._forwarders_only

    @forwarders_only.setter
    def forwarders_only(self, forwarders_only):
        """Sets the forwarders_only of this ConfigForwardNSG.

        Optional. True to only forward.  # noqa: E501

        :param forwarders_only: The forwarders_only of this ConfigForwardNSG.  # noqa: E501
        :type: bool
        """

        self._forwarders_only = forwarders_only

    @property
    def hosts(self):
        """Gets the hosts of this ConfigForwardNSG.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The hosts of this ConfigForwardNSG.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ConfigForwardNSG.

        The resource identifier.  # noqa: E501

        :param hosts: The hosts of this ConfigForwardNSG.  # noqa: E501
        :type: list[str]
        """

        self._hosts = hosts

    @property
    def id(self):
        """Gets the id of this ConfigForwardNSG.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The id of this ConfigForwardNSG.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigForwardNSG.

        The resource identifier.  # noqa: E501

        :param id: The id of this ConfigForwardNSG.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def internal_forwarders(self):
        """Gets the internal_forwarders of this ConfigForwardNSG.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The internal_forwarders of this ConfigForwardNSG.  # noqa: E501
        :rtype: list[str]
        """
        return self._internal_forwarders

    @internal_forwarders.setter
    def internal_forwarders(self, internal_forwarders):
        """Sets the internal_forwarders of this ConfigForwardNSG.

        The resource identifier.  # noqa: E501

        :param internal_forwarders: The internal_forwarders of this ConfigForwardNSG.  # noqa: E501
        :type: list[str]
        """

        self._internal_forwarders = internal_forwarders

    @property
    def name(self):
        """Gets the name of this ConfigForwardNSG.  # noqa: E501

        Required. Name of NSG object.  # noqa: E501

        :return: The name of this ConfigForwardNSG.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigForwardNSG.

        Required. Name of NSG object.  # noqa: E501

        :param name: The name of this ConfigForwardNSG.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nsgs(self):
        """Gets the nsgs of this ConfigForwardNSG.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The nsgs of this ConfigForwardNSG.  # noqa: E501
        :rtype: list[str]
        """
        return self._nsgs

    @nsgs.setter
    def nsgs(self, nsgs):
        """Sets the nsgs of this ConfigForwardNSG.

        The resource identifier.  # noqa: E501

        :param nsgs: The nsgs of this ConfigForwardNSG.  # noqa: E501
        :type: list[str]
        """

        self._nsgs = nsgs

    @property
    def tags(self):
        """Gets the tags of this ConfigForwardNSG.  # noqa: E501


        :return: The tags of this ConfigForwardNSG.  # noqa: E501
        :rtype: TypesJSONValue
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ConfigForwardNSG.


        :param tags: The tags of this ConfigForwardNSG.  # noqa: E501
        :type: TypesJSONValue
        """

        self._tags = tags

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
        if issubclass(ConfigForwardNSG, dict):
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
        if not isinstance(other, ConfigForwardNSG):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other