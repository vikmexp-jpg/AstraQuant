from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    """
    Represents the current open position.
    """

    symbol: str

    quantity: int

    average_price: float

    realized_pnl: float = 0.0

    unrealized_pnl: float = 0.0