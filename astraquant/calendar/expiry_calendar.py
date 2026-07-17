from __future__ import annotations

from datetime import date, timedelta


class ExpiryCalendar:
    """
    Weekly expiry calendar.

    Assumption:
    NIFTY weekly expiry = Tuesday
    """

    WEEKLY_EXPIRY = 1  # Monday=0, Tuesday=1

    @staticmethod
    def previous_expiry(today: date) -> date:
        """
        Returns the most recent weekly expiry.
        """

        days = (today.weekday() - ExpiryCalendar.WEEKLY_EXPIRY) % 7

        return today - timedelta(days=days)

    @staticmethod
    def next_expiry(today: date) -> date:
        """
        Returns the upcoming weekly expiry.
        """

        days = (ExpiryCalendar.WEEKLY_EXPIRY - today.weekday()) % 7

        if days == 0:
            days = 7

        return today + timedelta(days=days)

    @staticmethod
    def is_expiry_day(today: date) -> bool:
        return today.weekday() == ExpiryCalendar.WEEKLY_EXPIRY