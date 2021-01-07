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


class ConstraintStatus(object):
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
        'artifact_reference': 'str',
        'artifact_version': 'str',
        'comment': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'artifact_reference': 'artifactReference',
        'artifact_version': 'artifactVersion',
        'comment': 'comment',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, artifact_reference=None, artifact_version=None, comment=None, status=None, type=None):  # noqa: E501
        """ConstraintStatus - a model defined in Swagger"""  # noqa: E501

        self._artifact_reference = None
        self._artifact_version = None
        self._comment = None
        self._status = None
        self._type = None
        self.discriminator = None

        if artifact_reference is not None:
            self.artifact_reference = artifact_reference
        if artifact_version is not None:
            self.artifact_version = artifact_version
        if comment is not None:
            self.comment = comment
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def artifact_reference(self):
        """Gets the artifact_reference of this ConstraintStatus.  # noqa: E501


        :return: The artifact_reference of this ConstraintStatus.  # noqa: E501
        :rtype: str
        """
        return self._artifact_reference

    @artifact_reference.setter
    def artifact_reference(self, artifact_reference):
        """Sets the artifact_reference of this ConstraintStatus.


        :param artifact_reference: The artifact_reference of this ConstraintStatus.  # noqa: E501
        :type: str
        """

        self._artifact_reference = artifact_reference

    @property
    def artifact_version(self):
        """Gets the artifact_version of this ConstraintStatus.  # noqa: E501


        :return: The artifact_version of this ConstraintStatus.  # noqa: E501
        :rtype: str
        """
        return self._artifact_version

    @artifact_version.setter
    def artifact_version(self, artifact_version):
        """Sets the artifact_version of this ConstraintStatus.


        :param artifact_version: The artifact_version of this ConstraintStatus.  # noqa: E501
        :type: str
        """

        self._artifact_version = artifact_version

    @property
    def comment(self):
        """Gets the comment of this ConstraintStatus.  # noqa: E501


        :return: The comment of this ConstraintStatus.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ConstraintStatus.


        :param comment: The comment of this ConstraintStatus.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def status(self):
        """Gets the status of this ConstraintStatus.  # noqa: E501


        :return: The status of this ConstraintStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConstraintStatus.


        :param status: The status of this ConstraintStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this ConstraintStatus.  # noqa: E501


        :return: The type of this ConstraintStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConstraintStatus.


        :param type: The type of this ConstraintStatus.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ConstraintStatus, dict):
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
        if not isinstance(other, ConstraintStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other