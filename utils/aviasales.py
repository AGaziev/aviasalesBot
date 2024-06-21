import logging

import requests

from utils.ticket import FlightInfo


class AviasalesManager:
    request_prefix = "https://api.travelpayouts.com/aviasales/v3/"
    prices_for_dates = "prices_for_dates"

    def __init__(self, token):
        self.token = token

    def get_tickets_for_dates(self, origin: str, destination: str, departure_at: str, return_at: str,
                              unique: bool = False,
                              sorting: str = 'price', direct: bool = False, currency: str = 'rub', limit: int = 5,
                              page: int = 1, one_way: bool = True) -> dict:
        params = {
            'origin': origin,
            'destination': destination,
            'departure_at': departure_at,
            'return_at': return_at,
            'unique': str(unique).lower(),
            'sorting': sorting,
            'direct': str(direct).lower(),
            'currency': currency,
            'limit': limit,
            'page': page,
            'one_way': str(one_way).lower()
        }

        result = self.make_request(params, self.prices_for_dates)
        if result["success"] == False:
            logging.error("couldn't get tickets by some error", extra=params)
            return dict()
        logging.info(f"got tickets for currency {result['currency']}")
        ticketsRaw: list = result['data']
        tickets = []
        for ticketInfo in ticketsRaw:
            tickets.append(FlightInfo(**ticketInfo))
        logging.debug(tickets)
        return tickets

    def make_request(self, params: dict, method: str):
        base_url = self.request_prefix + method
        params['token'] = self.token
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
