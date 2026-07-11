from __future__ import annotations

from datetime import datetime

from astraquant.core.models import (
    Signal,
    Trade,
)


class TradeManager:
    """
    Handles the DIDRS trade lifecycle.
    Batch-1:
        • Entry confirmation only.
    """

    def __init__(self):

        self.current_trade: Trade | None = None

    def confirm_entry(
        self,
        signal: Signal,
        previous_high: float,
        current_high: float,
    ) -> Trade | None:
        """
        Confirm BUY only if the next candle
        breaks the previous candle HIGH.
        """

        if current_high <= previous_high:
            return None

        trade = Trade(
            symbol="NIFTY",
            entry_time=signal.timestamp,
            entry_price=signal.price,
            quantity=1,
        )

        self.current_trade = trade

        return trade