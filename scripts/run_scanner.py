from astraquant.broker.upstox import UpstoxBroker
from astraquant.scanners.discount_scanner import DiscountScanner
from astraquant.config.index_config import INDEX_CONFIG

broker = UpstoxBroker()

scanner = DiscountScanner(broker)

for symbol, config in INDEX_CONFIG.items():

    if not config["scan_enabled"]:
        continue

    try:

        scanner.scan(
            symbol=symbol,
            option_type="CE",
            interval="5minute",
            threshold=5,
        )

    except Exception as ex:

        print(f"{symbol} FAILED")
        print(ex)