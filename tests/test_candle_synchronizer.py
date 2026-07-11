from datetime import datetime

from astraquant.core.models import Candle
from astraquant.engine import CandleSynchronizer


def create_candle(timestamp: datetime, close: float) -> Candle:
    return Candle(
        timestamp=timestamp,
        open=100,
        high=110,
        low=90,
        close=close,
        volume=1000,
    )


def test_candle_synchronizer():

    t1 = datetime(2026, 1, 1, 9, 15)
    t2 = datetime(2026, 1, 1, 9, 20)

    spot = [
        create_candle(t1, 101),
        create_candle(t2, 102),
    ]

    option = [
        create_candle(t1, 201),
        create_candle(t2, 202),
    ]

    synchronized = CandleSynchronizer.synchronize(
        spot,
        option,
    )

    assert len(synchronized) == 2

    assert synchronized[0].spot.timestamp == synchronized[0].option.timestamp

    assert synchronized[1].spot.close == 102

    assert synchronized[1].option.close == 202