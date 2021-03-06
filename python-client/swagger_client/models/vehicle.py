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


class Vehicle(object):
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
        'lcolor': 'str',
        'prod_class': 'str',
        'bcolor': 'str',
        'direction': 'int',
        'name': 'str',
        'gid': 'str',
        'delay': 'int',
        'y': 'float',
        'x': 'float'
    }

    attribute_map = {
        'lcolor': 'lcolor',
        'prod_class': 'prodClass',
        'bcolor': 'bcolor',
        'direction': 'direction',
        'name': 'name',
        'gid': 'gid',
        'delay': 'delay',
        'y': 'y',
        'x': 'x'
    }

    def __init__(self, lcolor=None, prod_class=None, bcolor=None, direction=None, name=None, gid=None, delay=None, y=None, x=None):
        """
        Vehicle - a model defined in Swagger
        """

        self._lcolor = None
        self._prod_class = None
        self._bcolor = None
        self._direction = None
        self._name = None
        self._gid = None
        self._delay = None
        self._y = None
        self._x = None

        self.lcolor = lcolor
        self.prod_class = prod_class
        self.bcolor = bcolor
        self.direction = direction
        self.name = name
        self.gid = gid
        self.delay = delay
        self.y = y
        self.x = x

    @property
    def lcolor(self):
        """
        Gets the lcolor of this Vehicle.
        Line color of the journey

        :return: The lcolor of this Vehicle.
        :rtype: str
        """
        return self._lcolor

    @lcolor.setter
    def lcolor(self, lcolor):
        """
        Sets the lcolor of this Vehicle.
        Line color of the journey

        :param lcolor: The lcolor of this Vehicle.
        :type: str
        """
        if lcolor is None:
            raise ValueError("Invalid value for `lcolor`, must not be `None`")

        self._lcolor = lcolor

    @property
    def prod_class(self):
        """
        Gets the prod_class of this Vehicle.
        Product class

        :return: The prod_class of this Vehicle.
        :rtype: str
        """
        return self._prod_class

    @prod_class.setter
    def prod_class(self, prod_class):
        """
        Sets the prod_class of this Vehicle.
        Product class

        :param prod_class: The prod_class of this Vehicle.
        :type: str
        """
        if prod_class is None:
            raise ValueError("Invalid value for `prod_class`, must not be `None`")
        allowed_values = ["VAS", "LDT", "REG", "BUS", "BOAT", "TRAM", "TAXI"]
        if prod_class not in allowed_values:
            raise ValueError(
                "Invalid value for `prod_class` ({0}), must be one of {1}"
                .format(prod_class, allowed_values)
            )

        self._prod_class = prod_class

    @property
    def bcolor(self):
        """
        Gets the bcolor of this Vehicle.
        Background color of the journey

        :return: The bcolor of this Vehicle.
        :rtype: str
        """
        return self._bcolor

    @bcolor.setter
    def bcolor(self, bcolor):
        """
        Sets the bcolor of this Vehicle.
        Background color of the journey

        :param bcolor: The bcolor of this Vehicle.
        :type: str
        """
        if bcolor is None:
            raise ValueError("Invalid value for `bcolor`, must not be `None`")

        self._bcolor = bcolor

    @property
    def direction(self):
        """
        Gets the direction of this Vehicle.
        Direction of the vehicle. This is a value between 0 and 31 which is describing a direction vector

        :return: The direction of this Vehicle.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this Vehicle.
        Direction of the vehicle. This is a value between 0 and 31 which is describing a direction vector

        :param direction: The direction of this Vehicle.
        :type: int
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")

        self._direction = direction

    @property
    def name(self):
        """
        Gets the name of this Vehicle.
        Journey name

        :return: The name of this Vehicle.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Vehicle.
        Journey name

        :param name: The name of this Vehicle.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def gid(self):
        """
        Gets the gid of this Vehicle.
        Service GID

        :return: The gid of this Vehicle.
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """
        Sets the gid of this Vehicle.
        Service GID

        :param gid: The gid of this Vehicle.
        :type: str
        """
        if gid is None:
            raise ValueError("Invalid value for `gid`, must not be `None`")

        self._gid = gid

    @property
    def delay(self):
        """
        Gets the delay of this Vehicle.
        Current delay of the vehicle in minutes, can be negative, zero or positive

        :return: The delay of this Vehicle.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """
        Sets the delay of this Vehicle.
        Current delay of the vehicle in minutes, can be negative, zero or positive

        :param delay: The delay of this Vehicle.
        :type: int
        """
        if delay is None:
            raise ValueError("Invalid value for `delay`, must not be `None`")

        self._delay = delay

    @property
    def y(self):
        """
        Gets the y of this Vehicle.
        Y coordinate (latitude) of the position in WGS84 * 1000000

        :return: The y of this Vehicle.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y of this Vehicle.
        Y coordinate (latitude) of the position in WGS84 * 1000000

        :param y: The y of this Vehicle.
        :type: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")

        self._y = y

    @property
    def x(self):
        """
        Gets the x of this Vehicle.
        X coordinate (longitude) of the position in WGS84 * 1000000

        :return: The x of this Vehicle.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x of this Vehicle.
        X coordinate (longitude) of the position in WGS84 * 1000000

        :param x: The x of this Vehicle.
        :type: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")

        self._x = x

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
        if not isinstance(other, Vehicle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
