# coding: utf-8

"""
    Reseplaneraren

    Provides access to Västtrafik journey planner

    OpenAPI spec version: 1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SystemInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'timetable_info': 'TimetableInfo',
        'error_text': 'str',
        'error': 'str',
        'serverdate': 'date',
        'servertime': 'str',
        'no_namespace_schema_location': 'str'
    }

    attribute_map = {
        'timetable_info': 'TimetableInfo',
        'error_text': 'errorText',
        'error': 'error',
        'serverdate': 'serverdate',
        'servertime': 'servertime',
        'no_namespace_schema_location': 'noNamespaceSchemaLocation'
    }

    def __init__(self, timetable_info=None, error_text=None, error=None, serverdate=None, servertime=None, no_namespace_schema_location=None):
        """
        SystemInfo - a model defined in Swagger
        """

        self._timetable_info = None
        self._error_text = None
        self._error = None
        self._serverdate = None
        self._servertime = None
        self._no_namespace_schema_location = None

        if timetable_info is not None:
          self.timetable_info = timetable_info
        if error_text is not None:
          self.error_text = error_text
        if error is not None:
          self.error = error
        if serverdate is not None:
          self.serverdate = serverdate
        if servertime is not None:
          self.servertime = servertime
        self.no_namespace_schema_location = no_namespace_schema_location

    @property
    def timetable_info(self):
        """
        Gets the timetable_info of this SystemInfo.

        :return: The timetable_info of this SystemInfo.
        :rtype: TimetableInfo
        """
        return self._timetable_info

    @timetable_info.setter
    def timetable_info(self, timetable_info):
        """
        Sets the timetable_info of this SystemInfo.

        :param timetable_info: The timetable_info of this SystemInfo.
        :type: TimetableInfo
        """

        self._timetable_info = timetable_info

    @property
    def error_text(self):
        """
        Gets the error_text of this SystemInfo.

        :return: The error_text of this SystemInfo.
        :rtype: str
        """
        return self._error_text

    @error_text.setter
    def error_text(self, error_text):
        """
        Sets the error_text of this SystemInfo.

        :param error_text: The error_text of this SystemInfo.
        :type: str
        """

        self._error_text = error_text

    @property
    def error(self):
        """
        Gets the error of this SystemInfo.

        :return: The error of this SystemInfo.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this SystemInfo.

        :param error: The error of this SystemInfo.
        :type: str
        """

        self._error = error

    @property
    def serverdate(self):
        """
        Gets the serverdate of this SystemInfo.

        :return: The serverdate of this SystemInfo.
        :rtype: date
        """
        return self._serverdate

    @serverdate.setter
    def serverdate(self, serverdate):
        """
        Sets the serverdate of this SystemInfo.

        :param serverdate: The serverdate of this SystemInfo.
        :type: date
        """

        self._serverdate = serverdate

    @property
    def servertime(self):
        """
        Gets the servertime of this SystemInfo.
        Current server time in format HH:MM

        :return: The servertime of this SystemInfo.
        :rtype: str
        """
        return self._servertime

    @servertime.setter
    def servertime(self, servertime):
        """
        Sets the servertime of this SystemInfo.
        Current server time in format HH:MM

        :param servertime: The servertime of this SystemInfo.
        :type: str
        """

        self._servertime = servertime

    @property
    def no_namespace_schema_location(self):
        """
        Gets the no_namespace_schema_location of this SystemInfo.

        :return: The no_namespace_schema_location of this SystemInfo.
        :rtype: str
        """
        return self._no_namespace_schema_location

    @no_namespace_schema_location.setter
    def no_namespace_schema_location(self, no_namespace_schema_location):
        """
        Sets the no_namespace_schema_location of this SystemInfo.

        :param no_namespace_schema_location: The no_namespace_schema_location of this SystemInfo.
        :type: str
        """
        if no_namespace_schema_location is None:
            raise ValueError("Invalid value for `no_namespace_schema_location`, must not be `None`")

        self._no_namespace_schema_location = no_namespace_schema_location

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other