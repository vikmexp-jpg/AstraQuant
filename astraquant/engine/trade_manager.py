from __future__ import annotations

from astraquant.core.models import Signal, Trade
from astraquant.engine import SynchronizedCandle


class TradeManager:
    """
    Handles DIDRS trade lifecycle.

    Batch-1:
        • Pending BUY signal
        • Next candle confirmation
    """

    def __init__(self):

        self._pending_signal: Signal | None = None

        self.current_trade: Trade | None = None

    def register_signal(
        self,
        signal: Signal,
    ) -> None:
        """
        Store BUY signal.

        Entry is NOT taken immediately.
        """

        self._pending_signal = signal

    def process_next_candle(
        self,
        previous: SynchronizedCandle,
        current: SynchronizedCandle,
    ) -> Trade | None:
        """
        Confirm BUY only when
        current candle breaks
        previous candle HIGH.
        """

        if self._pending_signal is None:
            return None

        if current.spot.high <= previous.spot.high:
            return None

        trade = Trade(
            symbol="NIFTY",
            entry_time=current.spot.timestamp,
            entry_price=current.option.close,
            quantity=1,
        )

        self.current_trade = trade

        self._pending_signal = None

        return trade