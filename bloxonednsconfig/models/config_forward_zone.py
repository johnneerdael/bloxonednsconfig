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


class ConfigForwardZone(object):
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
        'disabled': 'bool',
        'external_forwarders': 'list[ConfigForwarder]',
        'forward_only': 'bool',
        'fqdn': 'str',
        'hosts': 'list[str]',
        'id': 'str',
        'internal_forwarders': 'list[str]',
        'mapped_subnet': 'str',
        'mapping': 'str',
        'nsgs': 'list[str]',
        'parent': 'str',
        'protocol_fqdn': 'str',
        'tags': 'TypesJSONValue',
        'view': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'disabled': 'disabled',
        'external_forwarders': 'external_forwarders',
        'forward_only': 'forward_only',
        'fqdn': 'fqdn',
        'hosts': 'hosts',
        'id': 'id',
        'internal_forwarders': 'internal_forwarders',
        'mapped_subnet': 'mapped_subnet',
        'mapping': 'mapping',
        'nsgs': 'nsgs',
        'parent': 'parent',
        'protocol_fqdn': 'protocol_fqdn',
        'tags': 'tags',
        'view': 'view'
    }

    def __init__(self, comment=None, disabled=None, external_forwarders=None, forward_only=None, fqdn=None, hosts=None, id=None, internal_forwarders=None, mapped_subnet=None, mapping=None, nsgs=None, parent=None, protocol_fqdn=None, tags=None, view=None):  # noqa: E501
        """ConfigForwardZone - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._disabled = None
        self._external_forwarders = None
        self._forward_only = None
        self._fqdn = None
        self._hosts = None
        self._id = None
        self._internal_forwarders = None
        self._mapped_subnet = None
        self._mapping = None
        self._nsgs = None
        self._parent = None
        self._protocol_fqdn = None
        self._tags = None
        self._view = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if disabled is not None:
            self.disabled = disabled
        if external_forwarders is not None:
            self.external_forwarders = external_forwarders
        if forward_only is not None:
            self.forward_only = forward_only
        self.fqdn = fqdn
        if hosts is not None:
            self.hosts = hosts
        if id is not None:
            self.id = id
        if internal_forwarders is not None:
            self.internal_forwarders = internal_forwarders
        if mapped_subnet is not None:
            self.mapped_subnet = mapped_subnet
        if mapping is not None:
            self.mapping = mapping
        if nsgs is not None:
            self.nsgs = nsgs
        if parent is not None:
            self.parent = parent
        if protocol_fqdn is not None:
            self.protocol_fqdn = protocol_fqdn
        if tags is not None:
            self.tags = tags
        if view is not None:
            self.view = view

    @property
    def comment(self):
        """Gets the comment of this ConfigForwardZone.  # noqa: E501

        Optional. Comment for zone configuration.  # noqa: E501

        :return: The comment of this ConfigForwardZone.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ConfigForwardZone.

        Optional. Comment for zone configuration.  # noqa: E501

        :param comment: The comment of this ConfigForwardZone.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def disabled(self):
        """Gets the disabled of this ConfigForwardZone.  # noqa: E501

        Optional. True to disable object. A disabled object is effectively non-existent when generating configuration.  # noqa: E501

        :return: The disabled of this ConfigForwardZone.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ConfigForwardZone.

        Optional. True to disable object. A disabled object is effectively non-existent when generating configuration.  # noqa: E501

        :param disabled: The disabled of this ConfigForwardZone.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def external_forwarders(self):
        """Gets the external_forwarders of this ConfigForwardZone.  # noqa: E501

        Optional. External DNS servers to forward to. Order is not significant.  # noqa: E501

        :return: The external_forwarders of this ConfigForwardZone.  # noqa: E501
        :rtype: list[ConfigForwarder]
        """
        return self._external_forwarders

    @external_forwarders.setter
    def external_forwarders(self, external_forwarders):
        """Sets the external_forwarders of this ConfigForwardZone.

        Optional. External DNS servers to forward to. Order is not significant.  # noqa: E501

        :param external_forwarders: The external_forwarders of this ConfigForwardZone.  # noqa: E501
        :type: list[ConfigForwarder]
        """

        self._external_forwarders = external_forwarders

    @property
    def forward_only(self):
        """Gets the forward_only of this ConfigForwardZone.  # noqa: E501

        Optional. True to only forward.  # noqa: E501

        :return: The forward_only of this ConfigForwardZone.  # noqa: E501
        :rtype: bool
        """
        return self._forward_only

    @forward_only.setter
    def forward_only(self, forward_only):
        """Sets the forward_only of this ConfigForwardZone.

        Optional. True to only forward.  # noqa: E501

        :param forward_only: The forward_only of this ConfigForwardZone.  # noqa: E501
        :type: bool
        """

        self._forward_only = forward_only

    @property
    def fqdn(self):
        """Gets the fqdn of this ConfigForwardZone.  # noqa: E501

        Required. Zone FQDN. The FQDN supplied at creation will be converted to canonical form. Read-only after creation.  # noqa: E501

        :return: The fqdn of this ConfigForwardZone.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this ConfigForwardZone.

        Required. Zone FQDN. The FQDN supplied at creation will be converted to canonical form. Read-only after creation.  # noqa: E501

        :param fqdn: The fqdn of this ConfigForwardZone.  # noqa: E501
        :type: str
        """
        if fqdn is None:
            raise ValueError("Invalid value for `fqdn`, must not be `None`")  # noqa: E501

        self._fqdn = fqdn

    @property
    def hosts(self):
        """Gets the hosts of this ConfigForwardZone.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The hosts of this ConfigForwardZone.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ConfigForwardZone.

        The resource identifier.  # noqa: E501

        :param hosts: The hosts of this ConfigForwardZone.  # noqa: E501
        :type: list[str]
        """

        self._hosts = hosts

    @property
    def id(self):
        """Gets the id of this ConfigForwardZone.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The id of this ConfigForwardZone.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigForwardZone.

        The resource identifier.  # noqa: E501

        :param id: The id of this ConfigForwardZone.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def internal_forwarders(self):
        """Gets the internal_forwarders of this ConfigForwardZone.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The internal_forwarders of this ConfigForwardZone.  # noqa: E501
        :rtype: list[str]
        """
        return self._internal_forwarders

    @internal_forwarders.setter
    def internal_forwarders(self, internal_forwarders):
        """Sets the internal_forwarders of this ConfigForwardZone.

        The resource identifier.  # noqa: E501

        :param internal_forwarders: The internal_forwarders of this ConfigForwardZone.  # noqa: E501
        :type: list[str]
        """

        self._internal_forwarders = internal_forwarders

    @property
    def mapped_subnet(self):
        """Gets the mapped_subnet of this ConfigForwardZone.  # noqa: E501

        Read-only. Reverse zone network address in the following format: <ip-address>/<cidr>. Defaults to empty.  # noqa: E501

        :return: The mapped_subnet of this ConfigForwardZone.  # noqa: E501
        :rtype: str
        """
        return self._mapped_subnet

    @mapped_subnet.setter
    def mapped_subnet(self, mapped_subnet):
        """Sets the mapped_subnet of this ConfigForwardZone.

        Read-only. Reverse zone network address in the following format: <ip-address>/<cidr>. Defaults to empty.  # noqa: E501

        :param mapped_subnet: The mapped_subnet of this ConfigForwardZone.  # noqa: E501
        :type: str
        """

        self._mapped_subnet = mapped_subnet

    @property
    def mapping(self):
        """Gets the mapping of this ConfigForwardZone.  # noqa: E501

        Read-only. Zone mapping type. Allowed values: - forward - ipv4_reverse Defaults to forward.  # noqa: E501

        :return: The mapping of this ConfigForwardZone.  # noqa: E501
        :rtype: str
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this ConfigForwardZone.

        Read-only. Zone mapping type. Allowed values: - forward - ipv4_reverse Defaults to forward.  # noqa: E501

        :param mapping: The mapping of this ConfigForwardZone.  # noqa: E501
        :type: str
        """

        self._mapping = mapping

    @property
    def nsgs(self):
        """Gets the nsgs of this ConfigForwardZone.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The nsgs of this ConfigForwardZone.  # noqa: E501
        :rtype: list[str]
        """
        return self._nsgs

    @nsgs.setter
    def nsgs(self, nsgs):
        """Sets the nsgs of this ConfigForwardZone.

        The resource identifier.  # noqa: E501

        :param nsgs: The nsgs of this ConfigForwardZone.  # noqa: E501
        :type: list[str]
        """

        self._nsgs = nsgs

    @property
    def parent(self):
        """Gets the parent of this ConfigForwardZone.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The parent of this ConfigForwardZone.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ConfigForwardZone.

        The resource identifier.  # noqa: E501

        :param parent: The parent of this ConfigForwardZone.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def protocol_fqdn(self):
        """Gets the protocol_fqdn of this ConfigForwardZone.  # noqa: E501

        Read only. Zone FQDN in punycode.  # noqa: E501

        :return: The protocol_fqdn of this ConfigForwardZone.  # noqa: E501
        :rtype: str
        """
        return self._protocol_fqdn

    @protocol_fqdn.setter
    def protocol_fqdn(self, protocol_fqdn):
        """Sets the protocol_fqdn of this ConfigForwardZone.

        Read only. Zone FQDN in punycode.  # noqa: E501

        :param protocol_fqdn: The protocol_fqdn of this ConfigForwardZone.  # noqa: E501
        :type: str
        """

        self._protocol_fqdn = protocol_fqdn

    @property
    def tags(self):
        """Gets the tags of this ConfigForwardZone.  # noqa: E501


        :return: The tags of this ConfigForwardZone.  # noqa: E501
        :rtype: TypesJSONValue
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ConfigForwardZone.


        :param tags: The tags of this ConfigForwardZone.  # noqa: E501
        :type: TypesJSONValue
        """

        self._tags = tags

    @property
    def view(self):
        """Gets the view of this ConfigForwardZone.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The view of this ConfigForwardZone.  # noqa: E501
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this ConfigForwardZone.

        The resource identifier.  # noqa: E501

        :param view: The view of this ConfigForwardZone.  # noqa: E501
        :type: str
        """

        self._view = view

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
        if issubclass(ConfigForwardZone, dict):
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
        if not isinstance(other, ConfigForwardZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other