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


class Leg(object):
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
        'fg_color': 'str',
        'booking': 'bool',
        'direction': 'str',
        'journey_detail_ref': 'JourneyDetailRef',
        'cancelled': 'bool',
        'kcal': 'float',
        'origin': 'Origin',
        'sname': 'str',
        'type': 'str',
        'geometry_ref': 'GeometryRef',
        'bg_color': 'str',
        'notes': 'Notes',
        'id': 'str',
        'stroke': 'str',
        'reachable': 'bool',
        'name': 'str',
        'night': 'bool',
        'destination': 'Destination',
        'percent_bike_road': 'float',
        'accessibility': 'str'
    }

    attribute_map = {
        'fg_color': 'fgColor',
        'booking': 'booking',
        'direction': 'direction',
        'journey_detail_ref': 'JourneyDetailRef',
        'cancelled': 'cancelled',
        'kcal': 'kcal',
        'origin': 'Origin',
        'sname': 'sname',
        'type': 'type',
        'geometry_ref': 'GeometryRef',
        'bg_color': 'bgColor',
        'notes': 'Notes',
        'id': 'id',
        'stroke': 'stroke',
        'reachable': 'reachable',
        'name': 'name',
        'night': 'night',
        'destination': 'Destination',
        'percent_bike_road': 'percentBikeRoad',
        'accessibility': 'accessibility'
    }

    def __init__(self, fg_color=None, booking=None, direction=None, journey_detail_ref=None, cancelled=None, kcal=None, origin=None, sname=None, type=None, geometry_ref=None, bg_color=None, notes=None, id=None, stroke=None, reachable=None, name=None, night=None, destination=None, percent_bike_road=None, accessibility=None):
        """
        Leg - a model defined in Swagger
        """

        self._fg_color = None
        self._booking = None
        self._direction = None
        self._journey_detail_ref = None
        self._cancelled = None
        self._kcal = None
        self._origin = None
        self._sname = None
        self._type = None
        self._geometry_ref = None
        self._bg_color = None
        self._notes = None
        self._id = None
        self._stroke = None
        self._reachable = None
        self._name = None
        self._night = None
        self._destination = None
        self._percent_bike_road = None
        self._accessibility = None

        if fg_color is not None:
          self.fg_color = fg_color
        if booking is not None:
          self.booking = booking
        if direction is not None:
          self.direction = direction
        if journey_detail_ref is not None:
          self.journey_detail_ref = journey_detail_ref
        if cancelled is not None:
          self.cancelled = cancelled
        if kcal is not None:
          self.kcal = kcal
        if origin is not None:
          self.origin = origin
        if sname is not None:
          self.sname = sname
        self.type = type
        if geometry_ref is not None:
          self.geometry_ref = geometry_ref
        if bg_color is not None:
          self.bg_color = bg_color
        if notes is not None:
          self.notes = notes
        if id is not None:
          self.id = id
        if stroke is not None:
          self.stroke = stroke
        if reachable is not None:
          self.reachable = reachable
        self.name = name
        if night is not None:
          self.night = night
        if destination is not None:
          self.destination = destination
        if percent_bike_road is not None:
          self.percent_bike_road = percent_bike_road
        if accessibility is not None:
          self.accessibility = accessibility

    @property
    def fg_color(self):
        """
        Gets the fg_color of this Leg.
        Foregroundcolor of this line

        :return: The fg_color of this Leg.
        :rtype: str
        """
        return self._fg_color

    @fg_color.setter
    def fg_color(self, fg_color):
        """
        Sets the fg_color of this Leg.
        Foregroundcolor of this line

        :param fg_color: The fg_color of this Leg.
        :type: str
        """

        self._fg_color = fg_color

    @property
    def booking(self):
        """
        Gets the booking of this Leg.
        Will be true if this journey needs to be booked

        :return: The booking of this Leg.
        :rtype: bool
        """
        return self._booking

    @booking.setter
    def booking(self, booking):
        """
        Sets the booking of this Leg.
        Will be true if this journey needs to be booked

        :param booking: The booking of this Leg.
        :type: bool
        """

        self._booking = booking

    @property
    def direction(self):
        """
        Gets the direction of this Leg.
        Direction information

        :return: The direction of this Leg.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this Leg.
        Direction information

        :param direction: The direction of this Leg.
        :type: str
        """

        self._direction = direction

    @property
    def journey_detail_ref(self):
        """
        Gets the journey_detail_ref of this Leg.

        :return: The journey_detail_ref of this Leg.
        :rtype: JourneyDetailRef
        """
        return self._journey_detail_ref

    @journey_detail_ref.setter
    def journey_detail_ref(self, journey_detail_ref):
        """
        Sets the journey_detail_ref of this Leg.

        :param journey_detail_ref: The journey_detail_ref of this Leg.
        :type: JourneyDetailRef
        """

        self._journey_detail_ref = journey_detail_ref

    @property
    def cancelled(self):
        """
        Gets the cancelled of this Leg.
        Will be true if this journey is cancelled

        :return: The cancelled of this Leg.
        :rtype: bool
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """
        Sets the cancelled of this Leg.
        Will be true if this journey is cancelled

        :param cancelled: The cancelled of this Leg.
        :type: bool
        """

        self._cancelled = cancelled

    @property
    def kcal(self):
        """
        Gets the kcal of this Leg.
        Energy use

        :return: The kcal of this Leg.
        :rtype: float
        """
        return self._kcal

    @kcal.setter
    def kcal(self, kcal):
        """
        Sets the kcal of this Leg.
        Energy use

        :param kcal: The kcal of this Leg.
        :type: float
        """

        self._kcal = kcal

    @property
    def origin(self):
        """
        Gets the origin of this Leg.

        :return: The origin of this Leg.
        :rtype: Origin
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this Leg.

        :param origin: The origin of this Leg.
        :type: Origin
        """

        self._origin = origin

    @property
    def sname(self):
        """
        Gets the sname of this Leg.
        Short name of the leg

        :return: The sname of this Leg.
        :rtype: str
        """
        return self._sname

    @sname.setter
    def sname(self, sname):
        """
        Sets the sname of this Leg.
        Short name of the leg

        :param sname: The sname of this Leg.
        :type: str
        """

        self._sname = sname

    @property
    def type(self):
        """
        Gets the type of this Leg.
        The attribute type specifies the type of the leg. Valid values are VAS, LDT (Long Distance Train), REG (Regional train), BUS , BOAT, TRAM, TAXI (Taxi/Telebus). Furthermore it can be of type WALK, BIKE and CAR if these legs are routes on the street network

        :return: The type of this Leg.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Leg.
        The attribute type specifies the type of the leg. Valid values are VAS, LDT (Long Distance Train), REG (Regional train), BUS , BOAT, TRAM, TAXI (Taxi/Telebus). Furthermore it can be of type WALK, BIKE and CAR if these legs are routes on the street network

        :param type: The type of this Leg.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def geometry_ref(self):
        """
        Gets the geometry_ref of this Leg.

        :return: The geometry_ref of this Leg.
        :rtype: GeometryRef
        """
        return self._geometry_ref

    @geometry_ref.setter
    def geometry_ref(self, geometry_ref):
        """
        Sets the geometry_ref of this Leg.

        :param geometry_ref: The geometry_ref of this Leg.
        :type: GeometryRef
        """

        self._geometry_ref = geometry_ref

    @property
    def bg_color(self):
        """
        Gets the bg_color of this Leg.
        Backgroundcolor of this line

        :return: The bg_color of this Leg.
        :rtype: str
        """
        return self._bg_color

    @bg_color.setter
    def bg_color(self, bg_color):
        """
        Sets the bg_color of this Leg.
        Backgroundcolor of this line

        :param bg_color: The bg_color of this Leg.
        :type: str
        """

        self._bg_color = bg_color

    @property
    def notes(self):
        """
        Gets the notes of this Leg.

        :return: The notes of this Leg.
        :rtype: Notes
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this Leg.

        :param notes: The notes of this Leg.
        :type: Notes
        """

        self._notes = notes

    @property
    def id(self):
        """
        Gets the id of this Leg.
        ID of the journey

        :return: The id of this Leg.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Leg.
        ID of the journey

        :param id: The id of this Leg.
        :type: str
        """

        self._id = id

    @property
    def stroke(self):
        """
        Gets the stroke of this Leg.
        Stroke style of this line

        :return: The stroke of this Leg.
        :rtype: str
        """
        return self._stroke

    @stroke.setter
    def stroke(self, stroke):
        """
        Sets the stroke of this Leg.
        Stroke style of this line

        :param stroke: The stroke of this Leg.
        :type: str
        """

        self._stroke = stroke

    @property
    def reachable(self):
        """
        Gets the reachable of this Leg.
        Will be true if this journey is not reachable due to delay of the feeder

        :return: The reachable of this Leg.
        :rtype: bool
        """
        return self._reachable

    @reachable.setter
    def reachable(self, reachable):
        """
        Sets the reachable of this Leg.
        Will be true if this journey is not reachable due to delay of the feeder

        :param reachable: The reachable of this Leg.
        :type: bool
        """

        self._reachable = reachable

    @property
    def name(self):
        """
        Gets the name of this Leg.
        The attribute name specifies the name of the leg

        :return: The name of this Leg.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Leg.
        The attribute name specifies the name of the leg

        :param name: The name of this Leg.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def night(self):
        """
        Gets the night of this Leg.
        Will be true if this journey is a night journey

        :return: The night of this Leg.
        :rtype: bool
        """
        return self._night

    @night.setter
    def night(self, night):
        """
        Sets the night of this Leg.
        Will be true if this journey is a night journey

        :param night: The night of this Leg.
        :type: bool
        """

        self._night = night

    @property
    def destination(self):
        """
        Gets the destination of this Leg.

        :return: The destination of this Leg.
        :rtype: Destination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this Leg.

        :param destination: The destination of this Leg.
        :type: Destination
        """

        self._destination = destination

    @property
    def percent_bike_road(self):
        """
        Gets the percent_bike_road of this Leg.
        Percentage of the route that is made up of bike roads

        :return: The percent_bike_road of this Leg.
        :rtype: float
        """
        return self._percent_bike_road

    @percent_bike_road.setter
    def percent_bike_road(self, percent_bike_road):
        """
        Sets the percent_bike_road of this Leg.
        Percentage of the route that is made up of bike roads

        :param percent_bike_road: The percent_bike_road of this Leg.
        :type: float
        """

        self._percent_bike_road = percent_bike_road

    @property
    def accessibility(self):
        """
        Gets the accessibility of this Leg.
        will only be set if the vehicle has wheelchair + ramp/lift or lowfloor according to realtime data

        :return: The accessibility of this Leg.
        :rtype: str
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility):
        """
        Sets the accessibility of this Leg.
        will only be set if the vehicle has wheelchair + ramp/lift or lowfloor according to realtime data

        :param accessibility: The accessibility of this Leg.
        :type: str
        """

        self._accessibility = accessibility

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
        if not isinstance(other, Leg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
