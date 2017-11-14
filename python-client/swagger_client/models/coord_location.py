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


class CoordLocation(object):
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
        'lon': 'str',
        'idx': 'str',
        'name': 'str',
        'type': 'str',
        'lat': 'str'
    }

    attribute_map = {
        'lon': 'lon',
        'idx': 'idx',
        'name': 'name',
        'type': 'type',
        'lat': 'lat'
    }

    def __init__(self, lon=None, idx=None, name=None, type=None, lat=None):
        """
        CoordLocation - a model defined in Swagger
        """

        self._lon = None
        self._idx = None
        self._name = None
        self._type = None
        self._lat = None

        self.lon = lon
        self.idx = idx
        self.name = name
        self.type = type
        self.lat = lat

    @property
    def lon(self):
        """
        Gets the lon of this CoordLocation.
        The WGS84 longitude

        :return: The lon of this CoordLocation.
        :rtype: str
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """
        Sets the lon of this CoordLocation.
        The WGS84 longitude

        :param lon: The lon of this CoordLocation.
        :type: str
        """
        if lon is None:
            raise ValueError("Invalid value for `lon`, must not be `None`")

        self._lon = lon

    @property
    def idx(self):
        """
        Gets the idx of this CoordLocation.
        This index can be used to reorder the StopLocations and CoordLocations in JSON format response to their correct order. IN JSON you can receive two arrays, one for Stops and one for Addresses. This attribute is only contained in reponses to the location.name request. The location with idx=1 is the best fitting location.

        :return: The idx of this CoordLocation.
        :rtype: str
        """
        return self._idx

    @idx.setter
    def idx(self, idx):
        """
        Sets the idx of this CoordLocation.
        This index can be used to reorder the StopLocations and CoordLocations in JSON format response to their correct order. IN JSON you can receive two arrays, one for Stops and one for Addresses. This attribute is only contained in reponses to the location.name request. The location with idx=1 is the best fitting location.

        :param idx: The idx of this CoordLocation.
        :type: str
        """
        if idx is None:
            raise ValueError("Invalid value for `idx`, must not be `None`")

        self._idx = idx

    @property
    def name(self):
        """
        Gets the name of this CoordLocation.
        Contains the output name of the address or point of interest

        :return: The name of this CoordLocation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CoordLocation.
        Contains the output name of the address or point of interest

        :param name: The name of this CoordLocation.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this CoordLocation.
        The attribute type specifies the type of location. Valid values are ADR (address) or POI (point of interest). This attribute can be used to do some sort of classification in the user interface. For later trip requests it does not have any meaning.

        :return: The type of this CoordLocation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CoordLocation.
        The attribute type specifies the type of location. Valid values are ADR (address) or POI (point of interest). This attribute can be used to do some sort of classification in the user interface. For later trip requests it does not have any meaning.

        :param type: The type of this CoordLocation.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def lat(self):
        """
        Gets the lat of this CoordLocation.
        The WGS84 latitude

        :return: The lat of this CoordLocation.
        :rtype: str
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """
        Sets the lat of this CoordLocation.
        The WGS84 latitude

        :param lat: The lat of this CoordLocation.
        :type: str
        """
        if lat is None:
            raise ValueError("Invalid value for `lat`, must not be `None`")

        self._lat = lat

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
        if not isinstance(other, CoordLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
