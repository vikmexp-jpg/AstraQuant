from datetime import datetime

from astraquant.core.models import (
    Signal,
    SignalType,
)
from astraquant.engine import TradeManager


def test_ignore_duplicate_signal():

    manager = TradeManager()

    signal = Signal(
        timestamp=datetime.now(),
        signal=SignalType.BUY,
        price=100,
        strategy="DIDRS",
        reason="Test",
    )

    manager.register_signal(signal)

    first = manager._pending_signal

    # Register same signal again
    manager.register_signal(signal)

    assert manager._pending_signal is first