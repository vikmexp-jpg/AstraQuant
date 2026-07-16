from dataclasses import dataclass


@dataclass(slots=True)
class MarketQuote:
    instrument: str
    ltp: float


@dataclass(slots=True)
class BrokerOrder:
    instrument: str
    quantity: int
    price: float
    side: str


@dataclass(slots=True)
class BrokerPosition:
    instrument: str
    quantity: int
    average_price: float