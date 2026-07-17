from datetime import datetime, timedelta

from astraquant.core.models import Candle
from astraquant.data.candle_aggregator import CandleAggregator


def candle(ts, price):

    return Candle(
        timestamp=ts,
        open=price,
        high=price + 2,
        low=price - 2,
        close=price + 1,
        volume=100,
    )


def test_aggregate_5_minutes():

    start = datetime(2026, 7, 17, 9, 15)

    candles = [
        candle(start + timedelta(minutes=i), 100 + i)
        for i in range(5)
    ]

    result = CandleAggregator.aggregate(
        candles,
        interval=5,
    )

    assert len(result) == 1

    c = result[0]

    assert c.open == 100
    assert c.close == 105
    assert c.high == 106
    assert c.low == 98
    assert c.volume == 500