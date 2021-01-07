# coding: utf-8

"""
    Spinnaker API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Headers(object):
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
        'invoke_headers': 'dict(str, str)',
        'read_headers': 'dict(str, str)',
        'write_headers': 'dict(str, str)'
    }

    attribute_map = {
        'invoke_headers': 'invokeHeaders',
        'read_headers': 'readHeaders',
        'write_headers': 'writeHeaders'
    }

    def __init__(self, invoke_headers=None, read_headers=None, write_headers=None):  # noqa: E501
        """Headers - a model defined in Swagger"""  # noqa: E501

        self._invoke_headers = None
        self._read_headers = None
        self._write_headers = None
        self.discriminator = None

        if invoke_headers is not None:
            self.invoke_headers = invoke_headers
        if read_headers is not None:
            self.read_headers = read_headers
        if write_headers is not None:
            self.write_headers = write_headers

    @property
    def invoke_headers(self):
        """Gets the invoke_headers of this Headers.  # noqa: E501


        :return: The invoke_headers of this Headers.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._invoke_headers

    @invoke_headers.setter
    def invoke_headers(self, invoke_headers):
        """Sets the invoke_headers of this Headers.


        :param invoke_headers: The invoke_headers of this Headers.  # noqa: E501
        :type: dict(str, str)
        """

        self._invoke_headers = invoke_headers

    @property
    def read_headers(self):
        """Gets the read_headers of this Headers.  # noqa: E501


        :return: The read_headers of this Headers.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._read_headers

    @read_headers.setter
    def read_headers(self, read_headers):
        """Sets the read_headers of this Headers.


        :param read_headers: The read_headers of this Headers.  # noqa: E501
        :type: dict(str, str)
        """

        self._read_headers = read_headers

    @property
    def write_headers(self):
        """Gets the write_headers of this Headers.  # noqa: E501


        :return: The write_headers of this Headers.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._write_headers

    @write_headers.setter
    def write_headers(self, write_headers):
        """Sets the write_headers of this Headers.


        :param write_headers: The write_headers of this Headers.  # noqa: E501
        :type: dict(str, str)
        """

        self._write_headers = write_headers

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
        if issubclass(Headers, dict):
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
        if not isinstance(other, Headers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
