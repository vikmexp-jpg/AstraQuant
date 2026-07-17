from .alert import Alert


class ConsoleAlert:

    @staticmethod
    def send(alert: Alert):

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