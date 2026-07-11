from datetime import datetime

from astraquant.core.models import Signal, SignalType


def test_buy_signal():

    signal = Signal(
        timestamp=datetime.now(),
        signal=SignalType.BUY,
        price=250.5,
        strategy="DIDRS",
        reason="Discount confirmed",
    )

    assert signal.signal == SignalType.BUY
    assert signal.strategy == "DIDRS"