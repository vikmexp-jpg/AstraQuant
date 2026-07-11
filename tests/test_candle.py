from datetime import datetime

from astraquant.core.models import Candle


def test_red_candle():

    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=105,
        low=95,
        close=98,
        volume=1000,
    )

    assert candle.is_red
    assert not candle.is_green
    assert candle.body == 2
    assert candle.range == 10


def test_green_candle():

    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=110,
        low=99,
        close=108,
        volume=500,
    )

    assert candle.is_green