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


class Destination(object):
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
        'route_idx': 'str',
        'value': 'str',
        'cancelled': 'bool',
        'track': 'str',
        'rt_track': 'str',
        'type': 'str',
        'date': 'date',
        'notes': 'Notes',
        'id': 'str',
        'rt_date': 'date',
        'time': 'str',
        'directdate': 'date',
        'name': 'str',
        'rt_time': 'str',
        'directtime': 'str'
    }

    attribute_map = {
        'route_idx': 'routeIdx',
        'value': '$',
        'cancelled': 'cancelled',
        'track': 'track',
        'rt_track': 'rtTrack',
        'type': 'type',
        'date': 'date',
        'notes': 'Notes',
        'id': 'id',
        'rt_date': 'rtDate',
        'time': 'time',
        'directdate': 'directdate',
        'name': 'name',
        'rt_time': 'rtTime',
        'directtime': 'directtime'
    }

    def __init__(self, route_idx=None, value=None, cancelled=None, track=None, rt_track=None, type=None, date=None, notes=None, id=None, rt_date=None, time=None, directdate=None, name=None, rt_time=None, directtime=None):
        """
        Destination - a model defined in Swagger
        """

        self._route_idx = None
        self._value = None
        self._cancelled = None
        self._track = None
        self._rt_track = None
        self._type = None
        self._date = None
        self._notes = None
        self._id = None
        self._rt_date = None
        self._time = None
        self._directdate = None
        self._name = None
        self._rt_time = None
        self._directtime = None

        if route_idx is not None:
          self.route_idx = route_idx
        self.value = value
        if cancelled is not None:
          self.cancelled = cancelled
        if track is not None:
          self.track = track
        if rt_track is not None:
          self.rt_track = rt_track
        self.type = type
        self.date = date
        if notes is not None:
          self.notes = notes
        self.id = id
        if rt_date is not None:
          self.rt_date = rt_date
        self.time = time
        if directdate is not None:
          self.directdate = directdate
        self.name = name
        if rt_time is not None:
          self.rt_time = rt_time
        if directtime is not None:
          self.directtime = directtime

    @property
    def route_idx(self):
        """
        Gets the route_idx of this Destination.
        Route index of a stop/station. Can be used as a reference of the stop/station in a journeyDetail response

        :return: The route_idx of this Destination.
        :rtype: str
        """
        return self._route_idx

    @route_idx.setter
    def route_idx(self, route_idx):
        """
        Sets the route_idx of this Destination.
        Route index of a stop/station. Can be used as a reference of the stop/station in a journeyDetail response

        :param route_idx: The route_idx of this Destination.
        :type: str
        """

        self._route_idx = route_idx

    @property
    def value(self):
        """
        Gets the value of this Destination.

        :return: The value of this Destination.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Destination.

        :param value: The value of this Destination.
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

    @property
    def cancelled(self):
        """
        Gets the cancelled of this Destination.
        Will be set to true if departure/arrival at this stop is cancelled

        :return: The cancelled of this Destination.
        :rtype: bool
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """
        Sets the cancelled of this Destination.
        Will be set to true if departure/arrival at this stop is cancelled

        :param cancelled: The cancelled of this Destination.
        :type: bool
        """

        self._cancelled = cancelled

    @property
    def track(self):
        """
        Gets the track of this Destination.
        Track information, if available

        :return: The track of this Destination.
        :rtype: str
        """
        return self._track

    @track.setter
    def track(self, track):
        """
        Sets the track of this Destination.
        Track information, if available

        :param track: The track of this Destination.
        :type: str
        """

        self._track = track

    @property
    def rt_track(self):
        """
        Gets the rt_track of this Destination.
        Realtime track information, if available

        :return: The rt_track of this Destination.
        :rtype: str
        """
        return self._rt_track

    @rt_track.setter
    def rt_track(self, rt_track):
        """
        Sets the rt_track of this Destination.
        Realtime track information, if available

        :param rt_track: The rt_track of this Destination.
        :type: str
        """

        self._rt_track = rt_track

    @property
    def type(self):
        """
        Gets the type of this Destination.
        The attribute type specifies the type of location. Valid values are ST (stop/station), ADR (address) or POI (point of interest)

        :return: The type of this Destination.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Destination.
        The attribute type specifies the type of location. Valid values are ST (stop/station), ADR (address) or POI (point of interest)

        :param type: The type of this Destination.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def date(self):
        """
        Gets the date of this Destination.
        Date in format YYYY-MM-DD

        :return: The date of this Destination.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this Destination.
        Date in format YYYY-MM-DD

        :param date: The date of this Destination.
        :type: date
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")

        self._date = date

    @property
    def notes(self):
        """
        Gets the notes of this Destination.

        :return: The notes of this Destination.
        :rtype: Notes
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this Destination.

        :param notes: The notes of this Destination.
        :type: Notes
        """

        self._notes = notes

    @property
    def id(self):
        """
        Gets the id of this Destination.
        ID of this stop

        :return: The id of this Destination.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Destination.
        ID of this stop

        :param id: The id of this Destination.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def rt_date(self):
        """
        Gets the rt_date of this Destination.
        Realtime date in format YYYY-MM-DD, if available

        :return: The rt_date of this Destination.
        :rtype: date
        """
        return self._rt_date

    @rt_date.setter
    def rt_date(self, rt_date):
        """
        Sets the rt_date of this Destination.
        Realtime date in format YYYY-MM-DD, if available

        :param rt_date: The rt_date of this Destination.
        :type: date
        """

        self._rt_date = rt_date

    @property
    def time(self):
        """
        Gets the time of this Destination.
        Time in format HH:MM

        :return: The time of this Destination.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this Destination.
        Time in format HH:MM

        :param time: The time of this Destination.
        :type: str
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")

        self._time = time

    @property
    def directdate(self):
        """
        Gets the directdate of this Destination.
        Date in format YYYY-MM-DD.  Based on the direct travel time

        :return: The directdate of this Destination.
        :rtype: date
        """
        return self._directdate

    @directdate.setter
    def directdate(self, directdate):
        """
        Sets the directdate of this Destination.
        Date in format YYYY-MM-DD.  Based on the direct travel time

        :param directdate: The directdate of this Destination.
        :type: date
        """

        self._directdate = directdate

    @property
    def name(self):
        """
        Gets the name of this Destination.
        Contains the name of the location

        :return: The name of this Destination.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Destination.
        Contains the name of the location

        :param name: The name of this Destination.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def rt_time(self):
        """
        Gets the rt_time of this Destination.
        Realtime time in format HH:MM if available

        :return: The rt_time of this Destination.
        :rtype: str
        """
        return self._rt_time

    @rt_time.setter
    def rt_time(self, rt_time):
        """
        Sets the rt_time of this Destination.
        Realtime time in format HH:MM if available

        :param rt_time: The rt_time of this Destination.
        :type: str
        """

        self._rt_time = rt_time

    @property
    def directtime(self):
        """
        Gets the directtime of this Destination.
        Direct Time format HH:MM. Based on the direct travel time

        :return: The directtime of this Destination.
        :rtype: str
        """
        return self._directtime

    @directtime.setter
    def directtime(self, directtime):
        """
        Sets the directtime of this Destination.
        Direct Time format HH:MM. Based on the direct travel time

        :param directtime: The directtime of this Destination.
        :type: str
        """

        self._directtime = directtime

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
        if not isinstance(other, Destination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
