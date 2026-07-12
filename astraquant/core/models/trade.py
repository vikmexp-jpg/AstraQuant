from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .trade_event import TradeEvent


class TradeStatus(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


@dataclass(slots=True)
class Trade:
    """
    Represents one trade.
    """

    symbol: str

    entry_time: datetime

    entry_price: float

    quantity: int

    status: TradeStatus = TradeStatus.OPEN

    exit_time: datetime | None = None

    exit_price: float | None = None

    pnl: float = 0.0
    events: list[TradeEvent] = field(
        default_factory=list,
    )

    def close(
        self,
        exit_time: datetime,
        exit_price: float,
    ) -> None:

        self.exit_time = exit_time

        self.exit_price = exit_price

        self.status = TradeStatus.CLOSED

        self.pnl = (
            exit_price - self.entry_price
        ) * self.quantity