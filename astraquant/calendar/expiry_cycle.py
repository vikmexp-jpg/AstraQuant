from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, time, timedelta

from astraquant.config.settings import DIDRS_SCAN_START, EXPIRY_ENTRY_CUTOFF
from astraquant.logger import logger

from .expiry_calendar import ExpiryCalendar


@dataclass(slots=True)
class ExpiryCycle:

    scan_start: datetime
    scan_end: datetime

    previous_expiry: datetime
    next_expiry: datetime

    is_expiry_day: bool
    allow_new_trade: bool

    @staticmethod
    def current(
        expiry_weekday: int,
    ) -> "ExpiryCycle":

        now = datetime.now().astimezone()
        today = now.date()

        is_expiry = ExpiryCalendar.is_expiry_day(
            today,
            expiry_weekday,
        )

        allow_trade = True

        if is_expiry:

            #
            # New DIDRS entries are allowed until 2:00 PM on expiry day.
            #
            cutoff = datetime.combine(
                today,
                EXPIRY_ENTRY_CUTOFF,
                tzinfo=now.tzinfo,
            )

            if now >= cutoff:
                allow_trade = False

        #
        # ------------------------------------------------------------
        # Determine previous expiry for the scan window.
        #
        # On expiry day BEFORE cutoff:
        #   Continue scanning the CURRENT expiry cycle.
        #
        # On expiry day AFTER cutoff:
        #   Previous expiry becomes today's expiry.
        #
        # On all other days:
        #   Use the normal previous expiry.
        # ------------------------------------------------------------
        #
        if is_expiry and allow_trade:

            previous_expiry = ExpiryCalendar.previous_expiry(
                today - timedelta(days=1),
                expiry_weekday,
            )

        else:

            previous_expiry = ExpiryCalendar.previous_expiry(
                today,
                expiry_weekday,
            )

        next_expiry = ExpiryCalendar.next_expiry(
            today,
            expiry_weekday,
        )

        #
        # Scan starts from the trading day after previous expiry.
        #
        scan_day = previous_expiry + timedelta(days=1)

        scan_start = datetime.combine(
            scan_day,
            DIDRS_SCAN_START,
            tzinfo=now.tzinfo,
        )

        #
        # Debug logs
        #
        logger.info("=" * 80)
        logger.info("EXPIRY CYCLE")
        logger.info("=" * 80)
        logger.info("Current Time      : %s", now)
        logger.info("Today             : %s", today)
        logger.info("Expiry Weekday    : %s", expiry_weekday)
        logger.info("Previous Expiry   : %s", previous_expiry)
        logger.info("Next Expiry       : %s", next_expiry)
        logger.info("Scan Day          : %s", scan_day)
        logger.info("Scan Start        : %s", scan_start)
        logger.info("Scan End          : %s", now)
        logger.info("Is Expiry Day     : %s", is_expiry)
        logger.info("Allow New Trade   : %s", allow_trade)
        logger.info("=" * 80)

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
            is_expiry_day=is_expiry,
            allow_new_trade=allow_trade,
        )