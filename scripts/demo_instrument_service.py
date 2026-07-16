from astraquant.broker.upstox import UpstoxBroker

broker = UpstoxBroker()

instrument = broker.instruments.find_option(
    symbol="NIFTY",
    strike=24000,
    option_type="CE",
)

print(instrument)