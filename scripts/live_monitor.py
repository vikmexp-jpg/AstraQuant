from __future__ import annotations

import time
from datetime import datetime

from astraquant.alerts.alert import Alert
from astraquant.alerts.alert_engine import AlertEngine
from astraquant.broker.upstox import UpstoxBroker
from astraquant.calendar.candle_scheduler import CandleScheduler
from astraquant.calendar.market_hours import MarketHours
from astraquant.config.index_config import INDEX_CONFIG
from astraquant.logger import logger
from astraquant.scanners.discount_scanner import DiscountScanner
from astraquant.signals.didrs_signal import DidrsSignal
from astraquant.didrs.didrs_engine import DidrsEngine
from astraquant.tracker import (
    DiscountSnapshot,
    DiscountTracker,
    OpportunityManager,
)

broker = UpstoxBroker()
engine = DidrsEngine(broker)


logger.info("=" * 80)
logger.info("ASTRAQUANT LIVE DIDRS MONITOR")
logger.info("=" * 80)


while True:

    now = datetime.now().astimezone()
    #
    # ------------------------------------------------------------
    # Market Closed
    # ------------------------------------------------------------
    #
    if not MarketHours.is_market_open(now):

        logger.info("Market Closed")
        logger.info("Current Time : %s", now.strftime("%Y-%m-%d %H:%M:%S"))

        next_open = MarketHours.next_market_open(now)

        sleep_seconds = (
            next_open - now
        ).total_seconds()

        hours = int(sleep_seconds // 3600)
        minutes = int((sleep_seconds % 3600) // 60)

        logger.info("Next Open    : %s", next_open)
        logger.info("Sleeping     : %dh %dm", hours, minutes)

        time.sleep(max(1, sleep_seconds))
        continue

    #
    # ------------------------------------------------------------
    # Wait for next completed candle
    # ------------------------------------------------------------
    #
    target = CandleScheduler.next_close(
        now,
        interval=5,
    )

    wait = max(
        1,
        (target - now).total_seconds(),
    )

    logger.info(
        "Next Scan : %s (%d sec)",
        target.strftime("%H:%M:%S"),
        int(wait),
    )

    time.sleep(wait)

    #
    # ------------------------------------------------------------
    # Scan all enabled indices
    # ------------------------------------------------------------
    #
    for symbol, config in INDEX_CONFIG.items():

        if not config.get("scan_enabled", False):
            continue

        threshold = config.get(
            "discount_threshold",
            5.0,
        )

        lifecycle = engine.run(
            symbol=symbol,
            threshold=threshold,
        )

        if lifecycle is None:
            continue

        logger.info(
            "[%s] %-11s %-8s Current=%6.2f Max=%6.2f",
            lifecycle.symbol,
            lifecycle.state.value,
            lifecycle.status.value,
            lifecycle.current_discount,
            lifecycle.max_discount,
        )