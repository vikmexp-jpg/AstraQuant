from __future__ import annotations

from datetime import datetime, timedelta


class CandleScheduler:
    """
    Scheduler for completed candles.
    """

    @staticmethod
    def next_close(
        now: datetime,
        interval: int = 5,
        delay_seconds: int = 10,
    ) -> datetime:
        """
        Returns the next completed candle time.

        Examples:
            09:17 -> 09:20:05
            09:20 -> 09:25:05
            15:27 -> 15:30:05
            23:58 -> 00:00:05 (next day)
        """

        # Remove seconds and microseconds
        current = now.replace(
            second=0,
            microsecond=0,
        )

        # Minutes to the next interval
        minutes_to_add = interval - (current.minute % interval)

        if minutes_to_add == 0:
            minutes_to_add = interval

        next_candle = current + timedelta(
            minutes=minutes_to_add,
        )

        return next_candle.replace(
            second=delay_seconds,
            microsecond=0,
        )