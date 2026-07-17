from astraquant.broker.upstox import UpstoxBroker

broker = UpstoxBroker()

candles = broker.history.get_historical_candles(
    instrument_key="NSE_INDEX|Nifty 50",
    to_date="2026-07-16",
)

print(f"Total candles: {len(candles)}")

print("First:", candles[0])
print("Last :", candles[-1])