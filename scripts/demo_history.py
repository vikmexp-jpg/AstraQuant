from astraquant.broker.upstox import UpstoxBroker

broker = UpstoxBroker()

candles = broker.history.get_intraday_candles(
    instrument_key="NSE_INDEX|Nifty 50",
    interval="5minute",
)

print(f"Total candles: {len(candles)}")

for candle in candles[-5:]:
    print(candle)