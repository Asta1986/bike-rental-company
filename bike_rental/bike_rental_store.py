"""This is the bike_rental_store module.
Provides the BikeRentalStore class.
"""


class BikeRentalStore:
    """Class that validates rental requests and registers clients with
    at least one rental.
    """
    __promotion = None
    __clients = None

    def __init__(self, promotion):
        """ Set new BikeRentalStore attributes.
        :param promotion: Promotion
        """
        self.__promotion = promotion
        self.__clients = []

    def handle_request(self, client, rentals):
        """Register the object that made the request and return the
        rental cost after applying promotional discounts if
        appropriate.
        :param client: Client
        :param rentals: tuple
        :return: float
        """
        self.__clients.append(client)
        return self.__promotion.apply_discount(rentals)
