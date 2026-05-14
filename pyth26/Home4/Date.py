# Date class
# Stores a month, day, and year


class Date:

    # Constructor
    def __init__(self, month, day, year):

        self._month = month
        self._day = day
        self._year = year

    # Getter for month
    @property
    def month(self):
        return self._month

    # Getter for day
    @property
    def day(self):
        return self._day

    # Getter for year
    @property
    def year(self):
        return self._year

    # Setter for month
    @month.setter
    def month(self, month):
        self._month = month

    # Setter for day
    @day.setter
    def day(self, day):
        self._day = day

    # Setter for year
    @year.setter
    def year(self, year):
        self._year = year

    # Compare two Date objects
    # Returns True if the dates are the same
    def __eq__(self, other):

        return (
            self._month == other.month and
            self._day == other.day and
            self._year == other.year
        )

    # String version of the Date object
    def __str__(self):

        return f"{self._month}/{self._day}/{self._year}"