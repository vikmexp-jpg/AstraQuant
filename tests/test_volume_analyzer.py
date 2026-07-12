from datetime import datetime

from astraquant.core.models import Candle
from astraquant.utils import VolumeAnalyzer


def candle(volume: int) -> Candle:
    return Candle(
        timestamp=datetime.now(),
        open=100,
        high=101,
        low=99,
        close=100,
        volume=volume,
    )


def test_average_volume():

    history = [
        candle(100),
        candle(200),
        candle(300),
        candle(400),
        candle(500),
    ]

    assert VolumeAnalyzer.average_volume(history) == 300


def test_volume_confirmation_true():

    history = [
        candle(100),
        candle(200),
        candle(300),
        candle(400),
        candle(500),
    ]

    assert VolumeAnalyzer.is_volume_confirmed(
        history,
        candle(600),
    )


def test_volume_confirmation_false():

    history = [
        candle(100),
        candle(200),
        candle(300),
        candle(400),
        candle(500),
    ]

    assert not VolumeAnalyzer.is_volume_confirmed(
        history,
        candle(250),
    )