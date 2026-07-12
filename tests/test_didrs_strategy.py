from datetime import datetime

from astraquant.core.models import Candle, SignalType
from astraquant.engine import SynchronizedCandle
from astraquant.strategies import DIDRSStrategy


def candle(open_, close_, volume):

    return Candle(
        timestamp=datetime.now(),
        open=open_,
        high=max(open_, close_),
        low=min(open_, close_),
        close=close_,
        volume=volume,
    )


def test_buy_signal():

    spot = candle(100, 95, 1000)

    option = candle(210, 190, 500)

    context = SynchronizedCandle(
        spot=spot,
        option=option,
    )

    strategy = DIDRSStrategy()

    history = [
        candle(210, 190, 100),
        candle(210, 190, 120),
        candle(210, 190, 140),
        candle(210, 190, 160),
        candle(210, 190, 180),
    ]

    signal = strategy.evaluate(
        context=context,
        expected_premium=220,
        strike=23500,
        previous_option_candles=history,
    )

    assert signal is not None

    assert signal.signal == SignalType.BUY

def test_buy_signal_rejected_due_to_low_volume():

    spot = candle(100, 95, 1000)

    # Current option volume = 130
    option = candle(210, 190, 130)

    context = SynchronizedCandle(
        spot=spot,
        option=option,
    )

    history = [
        candle(210, 190, 100),
        candle(210, 190, 120),
        candle(210, 190, 140),
        candle(210, 190, 160),
        candle(210, 190, 180),
    ]

    strategy = DIDRSStrategy()

    signal = strategy.evaluate(
        context=context,
        expected_premium=220,
        strike=23500,
        previous_option_candles=history,
    )

    assert signal is None