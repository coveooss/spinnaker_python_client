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


class ConstraintState(object):
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
        'artifact_version': 'str',
        'attributes': 'object',
        'comment': 'str',
        'created_at': 'str',
        'delivery_config_name': 'str',
        'environment_name': 'str',
        'judged_at': 'str',
        'judged_by': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'artifact_version': 'artifactVersion',
        'attributes': 'attributes',
        'comment': 'comment',
        'created_at': 'createdAt',
        'delivery_config_name': 'deliveryConfigName',
        'environment_name': 'environmentName',
        'judged_at': 'judgedAt',
        'judged_by': 'judgedBy',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, artifact_version=None, attributes=None, comment=None, created_at=None, delivery_config_name=None, environment_name=None, judged_at=None, judged_by=None, status=None, type=None):  # noqa: E501
        """ConstraintState - a model defined in Swagger"""  # noqa: E501

        self._artifact_version = None
        self._attributes = None
        self._comment = None
        self._created_at = None
        self._delivery_config_name = None
        self._environment_name = None
        self._judged_at = None
        self._judged_by = None
        self._status = None
        self._type = None
        self.discriminator = None

        if artifact_version is not None:
            self.artifact_version = artifact_version
        if attributes is not None:
            self.attributes = attributes
        if comment is not None:
            self.comment = comment
        if created_at is not None:
            self.created_at = created_at
        if delivery_config_name is not None:
            self.delivery_config_name = delivery_config_name
        if environment_name is not None:
            self.environment_name = environment_name
        if judged_at is not None:
            self.judged_at = judged_at
        if judged_by is not None:
            self.judged_by = judged_by
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def artifact_version(self):
        """Gets the artifact_version of this ConstraintState.  # noqa: E501


        :return: The artifact_version of this ConstraintState.  # noqa: E501
        :rtype: str
        """
        return self._artifact_version

    @artifact_version.setter
    def artifact_version(self, artifact_version):
        """Sets the artifact_version of this ConstraintState.


        :param artifact_version: The artifact_version of this ConstraintState.  # noqa: E501
        :type: str
        """

        self._artifact_version = artifact_version

    @property
    def attributes(self):
        """Gets the attributes of this ConstraintState.  # noqa: E501


        :return: The attributes of this ConstraintState.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ConstraintState.


        :param attributes: The attributes of this ConstraintState.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def comment(self):
        """Gets the comment of this ConstraintState.  # noqa: E501


        :return: The comment of this ConstraintState.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ConstraintState.


        :param comment: The comment of this ConstraintState.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created_at(self):
        """Gets the created_at of this ConstraintState.  # noqa: E501


        :return: The created_at of this ConstraintState.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConstraintState.


        :param created_at: The created_at of this ConstraintState.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def delivery_config_name(self):
        """Gets the delivery_config_name of this ConstraintState.  # noqa: E501


        :return: The delivery_config_name of this ConstraintState.  # noqa: E501
        :rtype: str
        """
        return self._delivery_config_name

    @delivery_config_name.setter
    def delivery_config_name(self, delivery_config_name):
        """Sets the delivery_config_name of this ConstraintState.


        :param delivery_config_name: The delivery_config_name of this ConstraintState.  # noqa: E501
        :type: str
        """

        self._delivery_config_name = delivery_config_name

    @property
    def environment_name(self):
        """Gets the environment_name of this ConstraintState.  # noqa: E501


        :return: The environment_name of this ConstraintState.  # noqa: E501
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this ConstraintState.


        :param environment_name: The environment_name of this ConstraintState.  # noqa: E501
        :type: str
        """

        self._environment_name = environment_name

    @property
    def judged_at(self):
        """Gets the judged_at of this ConstraintState.  # noqa: E501


        :return: The judged_at of this ConstraintState.  # noqa: E501
        :rtype: str
        """
        return self._judged_at

    @judged_at.setter
    def judged_at(self, judged_at):
        """Sets the judged_at of this ConstraintState.


        :param judged_at: The judged_at of this ConstraintState.  # noqa: E501
        :type: str
        """

        self._judged_at = judged_at

    @property
    def judged_by(self):
        """Gets the judged_by of this ConstraintState.  # noqa: E501


        :return: The judged_by of this ConstraintState.  # noqa: E501
        :rtype: str
        """
        return self._judged_by

    @judged_by.setter
    def judged_by(self, judged_by):
        """Sets the judged_by of this ConstraintState.


        :param judged_by: The judged_by of this ConstraintState.  # noqa: E501
        :type: str
        """

        self._judged_by = judged_by

    @property
    def status(self):
        """Gets the status of this ConstraintState.  # noqa: E501


        :return: The status of this ConstraintState.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConstraintState.


        :param status: The status of this ConstraintState.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this ConstraintState.  # noqa: E501


        :return: The type of this ConstraintState.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConstraintState.


        :param type: The type of this ConstraintState.  # noqa: E501
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
        if issubclass(ConstraintState, dict):
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
        if not isinstance(other, ConstraintState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
