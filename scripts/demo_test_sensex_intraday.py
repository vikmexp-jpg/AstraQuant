from astraquant.broker.upstox import UpstoxBroker

broker = UpstoxBroker()

print("=" * 80)
print("NIFTY")
print("=" * 80)

response = broker.history.history_api.get_intra_day_candle_data(
    instrument_key="NSE_INDEX|Nifty 50",
    interval="1minute",
    api_version="2.0",
)

print("Candles :", len(response.data.candles))

if response.data.candles:
    print("Latest :", response.data.candles[0])

print()

print("=" * 80)
print("SENSEX")
print("=" * 80)

response = broker.history.history_api.get_intra_day_candle_data(
    instrument_key="BSE_INDEX|SENSEX",
    interval="1minute",
    api_version="2.0",
)

print("Candles :", len(response.data.candles))

if response.data.candles:
    print("Latest :", response.data.candles[0])