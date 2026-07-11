from datetime import datetime

from astraquant.core.models import Candle
from astraquant.engine import PremiumCalculator


def test_expected_premium():

    candle = Candle(
        timestamp=datetime.now(),
        open=23600,
        high=23620,
        low=23580,
        close=23610,
        volume=1000,
    )

    premium = PremiumCalculator.expected_premium(
        candle,
        strike=23500,
    )

    assert premium == 130