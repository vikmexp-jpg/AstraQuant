from datetime import datetime

from astraquant.broker.upstox import UpstoxBroker

broker = UpstoxBroker()

start = datetime.fromisoformat(
    "2026-07-15T14:00:00+05:30"
)

end = datetime.fromisoformat(
    "2026-07-16T15:29:00+05:30"
)

candles = broker.history.get_historical_candles(
    instrument_key="NSE_INDEX|Nifty 50",
    to_date="2026-07-16",
    start_datetime=start,
    end_datetime=end,
)

print(f"Total Candles : {len(candles)}")

if candles:
    print("First :", candles[0].timestamp)
    print("Last  :", candles[-1].timestamp)