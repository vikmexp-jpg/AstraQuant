from __future__ import annotations

from datetime import datetime, timedelta, time


class MarketHours:
    """
    NSE / BSE Trading Hours
    """

    OPEN = time(9, 15)
    CLOSE = time(15, 30)

    @staticmethod
    def is_market_open(
        now: datetime,
    ) -> bool:

        if now.weekday() >= 5:
            return False

        current = now.time()

        return MarketHours.OPEN <= current < MarketHours.CLOSE

    @staticmethod
    def next_market_open(
        now: datetime,
    ) -> datetime:
        """
        Returns next market opening datetime.
        Weekends are skipped.
        """

        # Before market opens today
        if now.time() < MarketHours.OPEN:

            return datetime.combine(
                now.date(),
                MarketHours.OPEN,
                tzinfo=now.tzinfo,
            )

        # Otherwise move to next weekday
        next_day = now.date() + timedelta(days=1)

        while next_day.weekday() >= 5:
            next_day += timedelta(days=1)

        return datetime.combine(
            next_day,
            MarketHours.OPEN,
            tzinfo=now.tzinfo,
        )