from datetime import datetime

from astraquant.core.models import (
    TradeEvent,
    TradeEventType,
)


def test_trade_event():

    event = TradeEvent(
        timestamp=datetime.now(),
        event=TradeEventType.ENTRY,
        price=500,
        quantity=1,
        note="Initial entry",
    )

    assert event.event == TradeEventType.ENTRY
    assert event.price == 500
    assert event.quantity == 1