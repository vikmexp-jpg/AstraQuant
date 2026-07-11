from datetime import datetime

from astraquant.core.models import (
    Candle,
    Signal,
    SignalType,
)

from astraquant.engine import (
    CandleSynchronizer,
    TradeManager,
)


def candle(
    ts,
    close,
):

    return Candle(
        timestamp=ts,
        open=100,
        high=close,
        low=90,
        close=close,
        volume=1000,
    )


def test_target():

    ts = datetime(2026, 1, 1, 9, 15)

    signal = Signal(
        timestamp=ts,
        signal=SignalType.BUY,
        price=200,
        strategy="DIDRS",
        reason="Discount",
    )

    manager = TradeManager()

    manager.register_signal(signal)

    previous = CandleSynchronizer.synchronize(
        [candle(ts, 100)],
        [candle(ts, 200)],
    )[0]

    current = CandleSynchronizer.synchronize(
        [candle(ts, 111)],
        [candle(ts, 201)],
    )[0]

    manager.process_next_candle(
        previous,
        current,
    )

    target = CandleSynchronizer.synchronize(
        [candle(ts, 130)],
        [candle(ts, 231)],
    )[0]

    manager.manage_trade(target)

    assert manager.half_exit_done

    assert manager.break_even_enabled

    assert manager.trailing_stop == 221