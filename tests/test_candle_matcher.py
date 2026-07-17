from datetime import datetime

from astraquant.core.models import Candle
from astraquant.scanners.candle_matcher import CandleMatcher


def make(price, minute):

    return Candle(
        timestamp=datetime(2026, 7, 16, 9, minute),
        open=price,
        high=price,
        low=price,
        close=price,
        volume=1,
    )


def test_match():

    spot = [
        make(100, 15),
        make(101, 20),
    ]

    option = [
        make(10, 15),
        make(11, 20),
    ]

    result = CandleMatcher.match(
        spot,
        option,
    )

    assert len(result) == 2