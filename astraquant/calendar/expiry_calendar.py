from __future__ import annotations

from datetime import date, timedelta


class ExpiryCalendar:
    """
    Generic weekly expiry calendar.

    Weekday:
        Monday    = 0
        Tuesday   = 1
        Wednesday = 2
        Thursday  = 3
        Friday    = 4
    """

    @staticmethod
    def previous_expiry(
        today: date,
        expiry_weekday: int,
    ) -> date:
        """
        Returns the most recent weekly expiry.
        """

        days = (
            today.weekday() - expiry_weekday
        ) % 7

        return today - timedelta(days=days)

    @staticmethod
    def next_expiry(
        today: date,
        expiry_weekday: int,
    ) -> date:
        """
        Returns the upcoming weekly expiry.
        """

        days = (
            expiry_weekday - today.weekday()
        ) % 7

        if days == 0:
            days = 7

        return today + timedelta(days=days)

    @staticmethod
    def is_expiry_day(
        today: date,
        expiry_weekday: int,
    ) -> bool:

        return today.weekday() == expiry_weekday