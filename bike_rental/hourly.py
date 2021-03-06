"""This is the hourly module.
Provides the HourlyRental class.
"""
from bike_rental.rental import Rental
from datetime import datetime, timedelta


class HourlyRental(Rental):
    """Subclass of the Rental class that represents
    hourly rental.
    """
    @property
    def price(self):
        """:return: int"""
        return self._price

    def __init__(self, hours):
        """Set attributes of a new HourlyRental object.
        :param hours: int
        """
        self._price = self.unit_price() * hours
        self._start = datetime.now()
        self._end = self._start + timedelta(hours=hours)

    @staticmethod
    def unit_price():
        """Return the price of a one hour rental.
        :return: int"""
        return 5
