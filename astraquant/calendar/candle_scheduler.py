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
        delay_seconds: int = 5,
    ) -> datetime:
        """
        Returns the next completed candle time.

        Example:
            09:17 -> 09:20:05
            09:20 -> 09:25:05
            15:27 -> 15:30:05
        """

        minute = (
            ((now.minute // interval) + 1)
            * interval
        )

        if minute >= 60:

            return now.replace(
                hour=now.hour + 1,
                minute=0,
                second=delay_seconds,
                microsecond=0,
            )

        return now.replace(
            minute=minute,
            second=delay_seconds,
            microsecond=0,
        )