from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .trade_event import TradeEvent
from .trade_event import TradeEventType


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

        if not any(event.event == TradeEventType.ENTRY for event in self.events):
            self.events.append(
                TradeEvent(
                    timestamp=self.entry_time,
                    event=TradeEventType.ENTRY,
                    price=self.entry_price,
                    quantity=self.quantity,
                )
            )

        self.events.append(
            TradeEvent(
                timestamp=exit_time,
                event=TradeEventType.FINAL_EXIT,
                price=exit_price,
                quantity=self.quantity,
            )
        )
        self.status = TradeStatus.CLOSED

        self.pnl = self.calculate_realized_pnl()

    def calculate_realized_pnl(self) -> float:
        """
        Calculate realized P&L using trade events.
        """

        if not self.events:
            return self.pnl

        entry_event = next(
            (
                event
                for event in self.events
                if event.event.name == "ENTRY"
            ),
            None,
        )

        if entry_event is None:
            return self.pnl

        entry_price = entry_event.price
        realized = 0.0

        for event in self.events:

            if event.event.name in (
                "TARGET_50",
                "FINAL_EXIT",
            ):
                realized += (
                    event.price - entry_price
                ) * event.quantity

        return realized