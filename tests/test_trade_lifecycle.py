from datetime import datetime

from astraquant.core.models import (
    TradeEvent,
    TradeEventType,
)


def test_trade_event_types():

    event = TradeEvent(
        timestamp=datetime.now(),
        event=TradeEventType.ENTRY,
        price=500,
    )

    assert event.event == TradeEventType.ENTRY