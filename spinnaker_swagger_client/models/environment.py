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


class Environment(object):
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
        'constraints': 'list[Mapstringobject]',
        'locations': 'object',
        'name': 'str',
        'notifications': 'list[Notification]',
        'resources': 'list[Resource]'
    }

    attribute_map = {
        'constraints': 'constraints',
        'locations': 'locations',
        'name': 'name',
        'notifications': 'notifications',
        'resources': 'resources'
    }

    def __init__(self, constraints=None, locations=None, name=None, notifications=None, resources=None):  # noqa: E501
        """Environment - a model defined in Swagger"""  # noqa: E501

        self._constraints = None
        self._locations = None
        self._name = None
        self._notifications = None
        self._resources = None
        self.discriminator = None

        if constraints is not None:
            self.constraints = constraints
        if locations is not None:
            self.locations = locations
        if name is not None:
            self.name = name
        if notifications is not None:
            self.notifications = notifications
        if resources is not None:
            self.resources = resources

    @property
    def constraints(self):
        """Gets the constraints of this Environment.  # noqa: E501


        :return: The constraints of this Environment.  # noqa: E501
        :rtype: list[Mapstringobject]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this Environment.


        :param constraints: The constraints of this Environment.  # noqa: E501
        :type: list[Mapstringobject]
        """

        self._constraints = constraints

    @property
    def locations(self):
        """Gets the locations of this Environment.  # noqa: E501


        :return: The locations of this Environment.  # noqa: E501
        :rtype: object
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this Environment.


        :param locations: The locations of this Environment.  # noqa: E501
        :type: object
        """

        self._locations = locations

    @property
    def name(self):
        """Gets the name of this Environment.  # noqa: E501


        :return: The name of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Environment.


        :param name: The name of this Environment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notifications(self):
        """Gets the notifications of this Environment.  # noqa: E501


        :return: The notifications of this Environment.  # noqa: E501
        :rtype: list[Notification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this Environment.


        :param notifications: The notifications of this Environment.  # noqa: E501
        :type: list[Notification]
        """

        self._notifications = notifications

    @property
    def resources(self):
        """Gets the resources of this Environment.  # noqa: E501


        :return: The resources of this Environment.  # noqa: E501
        :rtype: list[Resource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Environment.


        :param resources: The resources of this Environment.  # noqa: E501
        :type: list[Resource]
        """

        self._resources = resources

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
        if issubclass(Environment, dict):
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
        if not isinstance(other, Environment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other