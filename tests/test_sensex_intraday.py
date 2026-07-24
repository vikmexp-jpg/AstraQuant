
from astraquant.broker.upstox import UpstoxBroker
from astraquant.pricing.strike_selector import StrikeSelector
from astraquant.config.index_config import INDEX_CONFIG

broker = UpstoxBroker()

cfg = INDEX_CONFIG["SENSEX"]

spot_key = cfg["spot_key"]

option = StrikeSelector.deep_itm_call(
    broker=broker,
    symbol="SENSEX",
)

print("=" * 80)
print("OPTION DETAILS")
print("=" * 80)
print("Instrument :", option.instrument_key)
print("Symbol     :", option.trading_symbol)
print()

candles = broker.history.get_intraday_candles(
    instrument_key=option.instrument_key,
    interval="1minute",
)

print("=" * 80)
print(f"Total Candles : {len(candles)}")
print("=" * 80)

print("First 20")
for c in candles[:20]:
    print(c.timestamp)

print()

print("Last 20")
for c in candles[-20:]:
    print(c.timestamp)