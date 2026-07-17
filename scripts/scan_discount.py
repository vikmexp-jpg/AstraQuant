from astraquant.broker.upstox import UpstoxBroker
from astraquant.scanners.discount_scanner import DiscountScanner

broker = UpstoxBroker()

scanner = DiscountScanner(broker)

scanner.scan(
    symbol="NIFTY",
    option_type="CE",
    interval="5minute",
    threshold=5,
)