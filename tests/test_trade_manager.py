from datetime import datetime

from astraquant.core.models import (
    Signal,
    SignalType,
)

from astraquant.engine import TradeManager


def test_entry_confirmation():

    signal = Signal(
        timestamp=datetime.now(),
        signal=SignalType.BUY,
        price=200,
        strategy="DIDRS",
        reason="Discount confirmed",
    )

    manager = TradeManager()

    trade = manager.confirm_entry(
        signal=signal,
        previous_high=110,
        current_high=111,
    )

    assert trade is not None

    assert trade.entry_price == 200