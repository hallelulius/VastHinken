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


class Direction(object):
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
        'route_idx_to': 'int',
        'value': 'str',
        'route_idx_from': 'int'
    }

    attribute_map = {
        'route_idx_to': 'routeIdxTo',
        'value': '$',
        'route_idx_from': 'routeIdxFrom'
    }

    def __init__(self, route_idx_to=None, value=None, route_idx_from=None):
        """
        Direction - a model defined in Swagger
        """

        self._route_idx_to = None
        self._value = None
        self._route_idx_from = None

        self.route_idx_to = route_idx_to
        self.value = value
        self.route_idx_from = route_idx_from

    @property
    def route_idx_to(self):
        """
        Gets the route_idx_to of this Direction.
        End of validity on total route

        :return: The route_idx_to of this Direction.
        :rtype: int
        """
        return self._route_idx_to

    @route_idx_to.setter
    def route_idx_to(self, route_idx_to):
        """
        Sets the route_idx_to of this Direction.
        End of validity on total route

        :param route_idx_to: The route_idx_to of this Direction.
        :type: int
        """
        if route_idx_to is None:
            raise ValueError("Invalid value for `route_idx_to`, must not be `None`")

        self._route_idx_to = route_idx_to

    @property
    def value(self):
        """
        Gets the value of this Direction.

        :return: The value of this Direction.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Direction.

        :param value: The value of this Direction.
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

    @property
    def route_idx_from(self):
        """
        Gets the route_idx_from of this Direction.
        Start of validity on total route

        :return: The route_idx_from of this Direction.
        :rtype: int
        """
        return self._route_idx_from

    @route_idx_from.setter
    def route_idx_from(self, route_idx_from):
        """
        Sets the route_idx_from of this Direction.
        Start of validity on total route

        :param route_idx_from: The route_idx_from of this Direction.
        :type: int
        """
        if route_idx_from is None:
            raise ValueError("Invalid value for `route_idx_from`, must not be `None`")

        self._route_idx_from = route_idx_from

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
        if not isinstance(other, Direction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
