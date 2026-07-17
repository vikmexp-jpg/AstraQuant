from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, time, timedelta

from .expiry_calendar import ExpiryCalendar


@dataclass
class ExpiryCycle:

    scan_start: datetime
    scan_end: datetime

    previous_expiry: datetime
    next_expiry: datetime

    is_expiry_day: bool
    allow_new_trade: bool

    @staticmethod
    def current():

        now = datetime.now().astimezone()

        today = now.date()

        previous_expiry = ExpiryCalendar.previous_expiry(today)

        next_expiry = ExpiryCalendar.next_expiry(today)

        # Scan starts from next trading day after expiry
        scan_day = previous_expiry + timedelta(days=1)

        scan_start = datetime.combine(
            scan_day,
            time(9, 15),
            tzinfo=now.tzinfo,
        )

        # Trading rule
        allow_trade = True

        if ExpiryCalendar.is_expiry_day(today):

            cutoff = datetime.combine(
                today,
                time(11, 0),
                tzinfo=now.tzinfo,
            )

            if now >= cutoff:
                allow_trade = False

        return ExpiryCycle(
            scan_start=scan_start,
            scan_end=now,
            previous_expiry=datetime.combine(
                previous_expiry,
                time(),
                tzinfo=now.tzinfo,
            ),
            next_expiry=datetime.combine(
                next_expiry,
                time(),
                tzinfo=now.tzinfo,
            ),
            is_expiry_day=ExpiryCalendar.is_expiry_day(today),
            allow_new_trade=allow_trade,
        )