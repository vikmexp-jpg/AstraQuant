from __future__ import annotations

from astraquant.core.models import Signal, Trade
from astraquant.engine import SynchronizedCandle
from datetime import time


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
        self._half_exit_done = False
        self._break_even = False
        self._trailing_stop: float | None = None
        self._reentry_allowed = True

    def register_signal(
        self,
        signal: Signal,
    ) -> None:
        """
        Store BUY signal.

        Entry is NOT taken immediately.
        """

        self._pending_signal = signal


    def manage_trade(
        self,
        current: SynchronizedCandle,
    ) -> None:
        """
        Manage an active trade.
        """

        if self.current_trade is None:
            return

        price = current.option.close

        entry = self.current_trade.entry_price

        profit = price - entry

        #
        # +30 Target
        #
        if (
            not self._half_exit_done
            and profit >= 30
        ):

            self._half_exit_done = True

            self._break_even = True

            self._trailing_stop = entry

            print(
                "[TARGET] Exit 50% "
                f"@ {price}"
            )

        #
        # Trail
        #
        if self._half_exit_done:

            new_stop = price - 10

            if (
                self._trailing_stop is None
                or new_stop > self._trailing_stop
            ):
                self._trailing_stop = new_stop


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
        
    def check_stop_loss(
        self,
        current: SynchronizedCandle,
    ) -> bool:
        """
        Exit trade only if candle closes below trailing stop.
        """

        if self.current_trade is None:
            return False

        if self._trailing_stop is None:
            return False

        if current.option.close >= self._trailing_stop:
            return False

        self.current_trade.close(
            exit_time=current.option.timestamp,
            exit_price=current.option.close,
        )

        self._reentry_allowed = True

        return True

    def check_end_of_day(
        self,
        current: SynchronizedCandle,
    ) -> bool:
        """
        Force exit at or after 3:20 PM.
        """

        if self.current_trade is None:
            return False

        if current.option.timestamp.time() < time(15, 20):
            return False

        self.current_trade.close(
            exit_time=current.option.timestamp,
            exit_price=current.option.close,
        )

        return True

    def reset_for_reentry(self) -> None:
        """
        Clear completed trade state.
        """

        self.current_trade = None

        self._pending_signal = None

        self._half_exit_done = False

        self._break_even = False

        self._trailing_stop = None



    @property
    def half_exit_done(self):

        return self._half_exit_done


    @property
    def break_even_enabled(self):

        return self._break_even


    @property
    def trailing_stop(self):

        return self._trailing_stop
    
    @property
    def reentry_allowed(self) -> bool:
        
        return self._reentry_allowed