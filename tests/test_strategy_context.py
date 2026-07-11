from datetime import datetime

from astraquant.core.models import Candle, StrategyContext


def test_strategy_context():

    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=110,
        low=90,
        close=95,
        volume=1000,
    )

    context = StrategyContext(
        spot=candle,
        option=candle,
        strike=23500,
        expected_premium=590,
        discount=30,
    )

    assert context.discount == 30