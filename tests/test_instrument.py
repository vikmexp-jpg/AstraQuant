from astraquant.broker import Instrument


def test_instrument():

    instrument = Instrument(
        instrument_key="NSE_FO|12345",
        trading_symbol="NIFTY24JUL23500CE",
        exchange="NSE_FO",
        symbol="NIFTY",
        expiry="2026-07-30",
        strike=23500,
        option_type="CE",
        lot_size=75,
    )

    assert instrument.symbol == "NIFTY"

    assert instrument.strike == 23500

    assert instrument.option_type == "CE"