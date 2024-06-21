import json
from datetime import datetime
from typing import Optional

class FlightInfo:
    def __init__(self, origin: str, destination: str, origin_airport: str, destination_airport: str, price: int,
                 airline: str, flight_number: str, departure_at: str, return_at: str, transfers: int,
                 return_transfers: int, duration: datetime, duration_to: datetime, duration_back: datetime, link: str):
        self.origin = origin
        self.destination = destination
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.price = price
        self.airline = airline
        self.flight_number = flight_number
        self.departure_at = datetime.fromisoformat(departure_at)
        self.return_at = datetime.fromisoformat(return_at)
        self.transfers = transfers
        self.return_transfers = return_transfers
        self.duration = duration
        self.duration_to = duration_to
        self.duration_back = duration_back
        self.link = link

    @classmethod
    def from_json(cls, json_str: str) -> 'FlightInfo':
        data = json.loads(json_str)
        return cls(**data)

    # def __repr__(self) -> str:
    #     return (f"FlightInfo(origin={self.origin}, destination={self.destination}, origin_airport={self.origin_airport}, "
    #             f"destination_airport={self.destination_airport}, price={self.price}, airline={self.airline}, "
    #             f"flight_number={self.flight_number}, departure_at={self.departure_at}, return_at={self.return_at}, "
    #             f"transfers={self.transfers}, return_transfers={self.return_transfers}, duration={self.duration}, "
    #             f"duration_to={self.duration_to}, duration_back={self.duration_back}, link={self.link})")

    def __repr__(self) -> str:
        return f"""Даты: {self.departure_at.strftime("%d.%m %H:%M")}-{self.return_at.strftime("%d.%m %H:%M")},
Цена: [{self.price}](https://www.aviasales.ru{self.link})"""