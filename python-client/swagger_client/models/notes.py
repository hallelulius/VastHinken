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


class Notes(object):
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
        'note': 'list[Note]'
    }

    attribute_map = {
        'note': 'Note'
    }

    def __init__(self, note=None):
        """
        Notes - a model defined in Swagger
        """

        self._note = None

        if note is not None:
          self.note = note

    @property
    def note(self):
        """
        Gets the note of this Notes.

        :return: The note of this Notes.
        :rtype: list[Note]
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this Notes.

        :param note: The note of this Notes.
        :type: list[Note]
        """

        self._note = note

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
        if not isinstance(other, Notes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
