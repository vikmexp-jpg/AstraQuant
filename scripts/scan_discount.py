from astraquant.broker.upstox import UpstoxBroker
from astraquant.scanners.discount_scanner import DiscountScanner

broker = UpstoxBroker()

scanner = DiscountScanner(broker)

scanner.scan(
    spot_key="NSE_INDEX|Nifty 50",
    symbol="NIFTY",
    option_type="CE",
    threshold=5,
)