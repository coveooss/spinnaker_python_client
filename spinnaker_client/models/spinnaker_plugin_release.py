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


class SpinnakerPluginRelease(object):
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
        '_date': 'datetime',
        'preferred': 'bool',
        'remote_extensions': 'list[RemoteExtensionConfig]',
        'requires': 'str',
        'sha512sum': 'str',
        'url': 'str',
        'version': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'preferred': 'preferred',
        'remote_extensions': 'remoteExtensions',
        'requires': 'requires',
        'sha512sum': 'sha512sum',
        'url': 'url',
        'version': 'version'
    }

    def __init__(self, _date=None, preferred=None, remote_extensions=None, requires=None, sha512sum=None, url=None, version=None):  # noqa: E501
        """SpinnakerPluginRelease - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._preferred = None
        self._remote_extensions = None
        self._requires = None
        self._sha512sum = None
        self._url = None
        self._version = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if preferred is not None:
            self.preferred = preferred
        if remote_extensions is not None:
            self.remote_extensions = remote_extensions
        if requires is not None:
            self.requires = requires
        if sha512sum is not None:
            self.sha512sum = sha512sum
        if url is not None:
            self.url = url
        if version is not None:
            self.version = version

    @property
    def _date(self):
        """Gets the _date of this SpinnakerPluginRelease.  # noqa: E501


        :return: The _date of this SpinnakerPluginRelease.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this SpinnakerPluginRelease.


        :param _date: The _date of this SpinnakerPluginRelease.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def preferred(self):
        """Gets the preferred of this SpinnakerPluginRelease.  # noqa: E501


        :return: The preferred of this SpinnakerPluginRelease.  # noqa: E501
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred):
        """Sets the preferred of this SpinnakerPluginRelease.


        :param preferred: The preferred of this SpinnakerPluginRelease.  # noqa: E501
        :type: bool
        """

        self._preferred = preferred

    @property
    def remote_extensions(self):
        """Gets the remote_extensions of this SpinnakerPluginRelease.  # noqa: E501


        :return: The remote_extensions of this SpinnakerPluginRelease.  # noqa: E501
        :rtype: list[RemoteExtensionConfig]
        """
        return self._remote_extensions

    @remote_extensions.setter
    def remote_extensions(self, remote_extensions):
        """Sets the remote_extensions of this SpinnakerPluginRelease.


        :param remote_extensions: The remote_extensions of this SpinnakerPluginRelease.  # noqa: E501
        :type: list[RemoteExtensionConfig]
        """

        self._remote_extensions = remote_extensions

    @property
    def requires(self):
        """Gets the requires of this SpinnakerPluginRelease.  # noqa: E501


        :return: The requires of this SpinnakerPluginRelease.  # noqa: E501
        :rtype: str
        """
        return self._requires

    @requires.setter
    def requires(self, requires):
        """Sets the requires of this SpinnakerPluginRelease.


        :param requires: The requires of this SpinnakerPluginRelease.  # noqa: E501
        :type: str
        """

        self._requires = requires

    @property
    def sha512sum(self):
        """Gets the sha512sum of this SpinnakerPluginRelease.  # noqa: E501


        :return: The sha512sum of this SpinnakerPluginRelease.  # noqa: E501
        :rtype: str
        """
        return self._sha512sum

    @sha512sum.setter
    def sha512sum(self, sha512sum):
        """Sets the sha512sum of this SpinnakerPluginRelease.


        :param sha512sum: The sha512sum of this SpinnakerPluginRelease.  # noqa: E501
        :type: str
        """

        self._sha512sum = sha512sum

    @property
    def url(self):
        """Gets the url of this SpinnakerPluginRelease.  # noqa: E501


        :return: The url of this SpinnakerPluginRelease.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SpinnakerPluginRelease.


        :param url: The url of this SpinnakerPluginRelease.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def version(self):
        """Gets the version of this SpinnakerPluginRelease.  # noqa: E501


        :return: The version of this SpinnakerPluginRelease.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SpinnakerPluginRelease.


        :param version: The version of this SpinnakerPluginRelease.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(SpinnakerPluginRelease, dict):
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
        if not isinstance(other, SpinnakerPluginRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other