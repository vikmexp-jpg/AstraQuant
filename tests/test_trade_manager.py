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


def candle(ts, high, close):

    return Candle(
        timestamp=ts,
        open=100,
        high=high,
        low=90,
        close=close,
        volume=1000,
    )


def test_trade_entry():

    ts1 = datetime(2026, 1, 1, 9, 15)
    ts2 = datetime(2026, 1, 1, 9, 20)

    previous = CandleSynchronizer.synchronize(
        [candle(ts1, 110, 95)],
        [candle(ts1, 210, 190)],
    )[0]

    current = CandleSynchronizer.synchronize(
        [candle(ts2, 111, 96)],
        [candle(ts2, 215, 195)],
    )[0]

    signal = Signal(
        timestamp=ts1,
        signal=SignalType.BUY,
        price=190,
        strategy="DIDRS",
        reason="Discount",
    )

    manager = TradeManager()

    manager.register_signal(signal)

    trade = manager.process_next_candle(
        previous,
        current,
    )

    assert trade is not None

    assert trade.entry_price == 195