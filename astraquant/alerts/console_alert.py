import logging

from .alert import Alert

logger = logging.getLogger("AstraQuant")


class ConsoleAlert:

    @staticmethod
    def send(alert: Alert):
        logger.info(f"Displaying console alert for {alert.symbol}")
        print()
        print("=" * 80)
        print("🚨 DIDRS ALERT")
        print("=" * 80)
        print(f"Index      : {alert.symbol}")
        print(f"Option     : {alert.option}")
        print(f"Signal     : {alert.signal}")
        print(f"Discount   : {alert.discount:.2f}")
        print(f"Time       : {alert.timestamp}")
        print("=" * 80)