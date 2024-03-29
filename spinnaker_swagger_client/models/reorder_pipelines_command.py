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


class ReorderPipelinesCommand(object):
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
        'application': 'str',
        'ids_to_indices': 'dict(str, int)'
    }

    attribute_map = {
        'application': 'application',
        'ids_to_indices': 'idsToIndices'
    }

    def __init__(self, application=None, ids_to_indices=None):  # noqa: E501
        """ReorderPipelinesCommand - a model defined in Swagger"""  # noqa: E501

        self._application = None
        self._ids_to_indices = None
        self.discriminator = None

        if application is not None:
            self.application = application
        if ids_to_indices is not None:
            self.ids_to_indices = ids_to_indices

    @property
    def application(self):
        """Gets the application of this ReorderPipelinesCommand.  # noqa: E501


        :return: The application of this ReorderPipelinesCommand.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ReorderPipelinesCommand.


        :param application: The application of this ReorderPipelinesCommand.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def ids_to_indices(self):
        """Gets the ids_to_indices of this ReorderPipelinesCommand.  # noqa: E501


        :return: The ids_to_indices of this ReorderPipelinesCommand.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._ids_to_indices

    @ids_to_indices.setter
    def ids_to_indices(self, ids_to_indices):
        """Sets the ids_to_indices of this ReorderPipelinesCommand.


        :param ids_to_indices: The ids_to_indices of this ReorderPipelinesCommand.  # noqa: E501
        :type: dict(str, int)
        """

        self._ids_to_indices = ids_to_indices

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
        if issubclass(ReorderPipelinesCommand, dict):
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
        if not isinstance(other, ReorderPipelinesCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
