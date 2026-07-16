from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"


class ProductType(Enum):
    INTRADAY = "INTRADAY"
    DELIVERY = "DELIVERY"

class TradingMode(Enum):
    PAPER = "PAPER"
    LIVE = "LIVE"


class OrderStatus(Enum):
    PENDING = "PENDING"
    COMPLETE = "COMPLETE"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"


@dataclass(slots=True)
class MarketQuote:
    instrument: str
    ltp: float


@dataclass(slots=True)
class BrokerOrder:
    instrument: Instrument

    quantity: int

    side: OrderSide

    order_type: OrderType

    product: ProductType

    price: float | None = None

    order_id: str | None = None

    status: OrderStatus = OrderStatus.PENDING


@dataclass(slots=True)
class BrokerPosition:
    instrument: str
    quantity: int
    average_price: float

@dataclass(slots=True)
class Instrument:
    """
    Tradable instrument.
    """

    instrument_key: str

    trading_symbol: str

    exchange: str

    symbol: str

    expiry: str

    strike: int | None

    option_type: str | None

    lot_size: int

class ExpiryType(Enum):
    CURRENT_WEEK = "CURRENT_WEEK"
    NEXT_WEEK = "NEXT_WEEK"
    CURRENT_MONTH = "CURRENT_MONTH"
    NEXT_MONTH = "NEXT_MONTH"