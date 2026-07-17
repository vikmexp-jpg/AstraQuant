from astraquant.broker.upstox import UpstoxBroker
from astraquant.data.candle_aggregator import CandleAggregator
from astraquant.scanners.discount_scanner import DiscountScanner

broker = UpstoxBroker()

# Spot candles
spot = broker.history.get_historical_candles(
    instrument_key="NSE_INDEX|Nifty 50",
    to_date="2026-07-16",
)

# TODO:
# Replace this with actual option instrument.
option = broker.history.get_historical_candles(
    instrument_key="NSE_FO|57340",
    to_date="2026-07-16",
)

spot = CandleAggregator.aggregate(
    spot,
    5,
)

option = CandleAggregator.aggregate(
    option,
    5,
)

DiscountScanner.scan(
    spot_candles=spot,
    option_candles=option,
    strike=24000,
)