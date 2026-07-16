from astraquant.broker.upstox import UpstoxBroker

broker = UpstoxBroker()

broker.connect()

quote = broker.get_quote(
    "NSE_INDEX|Nifty 50",
)

print("=" * 60)
print("Instrument :", quote.instrument)
print("LTP        :", quote.ltp)
print("=" * 60)