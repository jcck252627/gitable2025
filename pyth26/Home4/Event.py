# Import the Date class
from Date import Date


# Event class
# Stores information about one event


class Event:

    # Constructor
    def __init__(self, event_name, start_hour, end_hour, event_date):

        self._event_name = event_name
        self._start_hour = start_hour
        self._end_hour = end_hour
        self._event_date = event_date

    # Getter for event name
    @property
    def event_name(self):
        return self._event_name

    # Getter for start hour
    @property
    def start_hour(self):
        return self._start_hour

    # Getter for end hour
    @property
    def end_hour(self):
        return self._end_hour

    # Getter for event date
    @property
    def event_date(self):
        return self._event_date

    # Setter for event name
    @event_name.setter
    def event_name(self, event_name):
        self._event_name = event_name

    # Setter for start hour
    @start_hour.setter
    def start_hour(self, start_hour):
        self._start_hour = start_hour

    # Setter for end hour
    @end_hour.setter
    def end_hour(self, end_hour):
        self._end_hour = end_hour

    # Setter for event date
    @event_date.setter
    def event_date(self, event_date):
        self._event_date = event_date

    # String version of the Event object
    def __str__(self):

        return (
            f"Event Name: {self._event_name}\n"
            f"Date: {self._event_date}\n"
            f"Time: {self._start_hour} to {self._end_hour}"
        )