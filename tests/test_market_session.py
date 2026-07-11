from astraquant.core.models import MarketSession


def test_market_session():

    assert MarketSession.MARKET.value == "MARKET"