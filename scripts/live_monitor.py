from datetime import datetime
import time

from astraquant.alerts.telegram_alert import TelegramAlert
from astraquant.broker.upstox import UpstoxBroker
from astraquant.scanners.discount_scanner import DiscountScanner
from astraquant.config.index_config import INDEX_CONFIG
from astraquant.calendar.market_hours import MarketHours
from astraquant.calendar.candle_scheduler import CandleScheduler
from astraquant.signals.didrs_signal import DidrsSignal
from astraquant.alerts.alert import Alert
from astraquant.alerts.alert_engine import AlertEngine
from plyer import notification
from astraquant.logger import logger

broker = UpstoxBroker()
scanner = DiscountScanner(broker)

def next_scan_time(now: datetime) -> datetime:
    """
    Returns the next completed 5-minute candle time.
    Example:
        09:17 -> 09:20
        09:20 -> 09:25
    """

    minute = ((now.minute // 5) + 1) * 5

    if minute == 60:
        return now.replace(
            hour=now.hour + 1,
            minute=0,
            second=5,
            microsecond=0,
        )

    return now.replace(
        minute=minute,
        second=5,
        microsecond=0,
    )


logger.info("-" * 60)
logger.info("ASTRAQUANT LIVE DIDRS MONITOR")
logger.info("-" * 60)

while True:

    now = datetime.now().astimezone()

    if not MarketHours.is_market_open(now):

        print()
        print("=" * 80)
        print("MARKET CLOSED")
        print("Run: python scripts/run_scanner.py  # execute after market close")
        print("=" * 80)
        print(f"Current Time : {now.strftime('%Y-%m-%d %H:%M:%S')}")

        next_open = MarketHours.next_market_open(now)

        sleep_seconds = (
            next_open - now
        ).total_seconds()

        hours = int(sleep_seconds // 3600)
        minutes = int((sleep_seconds % 3600) // 60)

        print(f"Next Open   : {next_open}")
        print(f"Sleeping    : {hours}h {minutes}m")

        #time.sleep(max(1, sleep_seconds))
        #continue

        target = CandleScheduler.next_close(
            now,
            interval=5,
        )

        wait = (target - now).total_seconds()

        print()
        print(f"Current Time : {now.strftime('%H:%M:%S')}")
        print(f"Next Scan    : {target.strftime('%H:%M:%S')}")
        print(f"Sleeping     : {wait:.0f} sec")

        time.sleep(10)

        print()
        print("=" * 100)
        print(
            f"Scanning at {datetime.now().strftime('%H:%M:%S')}"
        )
        print("=" * 100)

        for symbol, config in INDEX_CONFIG.items():

            if not config["scan_enabled"]:
                continue

            threshold = config.get("discount_threshold", 5.0)

            result = scanner.scan(
                symbol=symbol,
                option_type="CE",
                interval="5minute",
                threshold=threshold,
            )
            #print(result)
            signal = DidrsSignal.generate(
                current_discount=result.current_discount,
                threshold=threshold,
            )

            alert = Alert(
                symbol=result.symbol,
                option=result.option_symbol,
                discount=result.current_discount,
                timestamp=result.top_discounts[0].timestamp if result.top_discounts else datetime.now(),
                signal=signal.action,
            )

            AlertEngine.notify(alert)