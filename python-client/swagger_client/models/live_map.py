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


class LiveMap(object):
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
        'time': 'date',
        'maxx': 'float',
        'maxy': 'float',
        'vehicles': 'list[Vehicle]',
        'minx': 'float',
        'miny': 'float'
    }

    attribute_map = {
        'time': 'time',
        'maxx': 'maxx',
        'maxy': 'maxy',
        'vehicles': 'vehicles',
        'minx': 'minx',
        'miny': 'miny'
    }

    def __init__(self, time=None, maxx=None, maxy=None, vehicles=None, minx=None, miny=None):
        """
        LiveMap - a model defined in Swagger
        """

        self._time = None
        self._maxx = None
        self._maxy = None
        self._vehicles = None
        self._minx = None
        self._miny = None

        self.time = time
        self.maxx = maxx
        self.maxy = maxy
        self.vehicles = vehicles
        self.minx = minx
        self.miny = miny

    @property
    def time(self):
        """
        Gets the time of this LiveMap.
        Current server time

        :return: The time of this LiveMap.
        :rtype: date
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this LiveMap.
        Current server time

        :param time: The time of this LiveMap.
        :type: date
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")

        self._time = time

    @property
    def maxx(self):
        """
        Gets the maxx of this LiveMap.
        Right border (longitude) of the bounding box in WGS84 * 1000000

        :return: The maxx of this LiveMap.
        :rtype: float
        """
        return self._maxx

    @maxx.setter
    def maxx(self, maxx):
        """
        Sets the maxx of this LiveMap.
        Right border (longitude) of the bounding box in WGS84 * 1000000

        :param maxx: The maxx of this LiveMap.
        :type: float
        """
        if maxx is None:
            raise ValueError("Invalid value for `maxx`, must not be `None`")

        self._maxx = maxx

    @property
    def maxy(self):
        """
        Gets the maxy of this LiveMap.
        Upper border (latitude) of the bounding box in WGS84 * 1000000

        :return: The maxy of this LiveMap.
        :rtype: float
        """
        return self._maxy

    @maxy.setter
    def maxy(self, maxy):
        """
        Sets the maxy of this LiveMap.
        Upper border (latitude) of the bounding box in WGS84 * 1000000

        :param maxy: The maxy of this LiveMap.
        :type: float
        """
        if maxy is None:
            raise ValueError("Invalid value for `maxy`, must not be `None`")

        self._maxy = maxy

    @property
    def vehicles(self):
        """
        Gets the vehicles of this LiveMap.

        :return: The vehicles of this LiveMap.
        :rtype: list[Vehicle]
        """
        return self._vehicles

    @vehicles.setter
    def vehicles(self, vehicles):
        """
        Sets the vehicles of this LiveMap.

        :param vehicles: The vehicles of this LiveMap.
        :type: list[Vehicle]
        """
        if vehicles is None:
            raise ValueError("Invalid value for `vehicles`, must not be `None`")

        self._vehicles = vehicles

    @property
    def minx(self):
        """
        Gets the minx of this LiveMap.
        Left border (longitude) of the bounding box in WGS84 * 1000000

        :return: The minx of this LiveMap.
        :rtype: float
        """
        return self._minx

    @minx.setter
    def minx(self, minx):
        """
        Sets the minx of this LiveMap.
        Left border (longitude) of the bounding box in WGS84 * 1000000

        :param minx: The minx of this LiveMap.
        :type: float
        """
        if minx is None:
            raise ValueError("Invalid value for `minx`, must not be `None`")

        self._minx = minx

    @property
    def miny(self):
        """
        Gets the miny of this LiveMap.
        Lower border (latitude) of the bounding box in WGS84 * 1000000

        :return: The miny of this LiveMap.
        :rtype: float
        """
        return self._miny

    @miny.setter
    def miny(self, miny):
        """
        Sets the miny of this LiveMap.
        Lower border (latitude) of the bounding box in WGS84 * 1000000

        :param miny: The miny of this LiveMap.
        :type: float
        """
        if miny is None:
            raise ValueError("Invalid value for `miny`, must not be `None`")

        self._miny = miny

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
        if not isinstance(other, LiveMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
