from datetime import datetime

from astraquant.core.models import (
    TradeEvent,
    TradeEventType,
)
from datetime import datetime

from astraquant.core.models import (
    Trade,
    TradeEventType,
)


def test_trade_event():

    event = TradeEvent(
        timestamp=datetime.now(),
        event=TradeEventType.ENTRY,
        price=500,
        quantity=1,
    )

    assert event.event == TradeEventType.ENTRY

    assert event.price == 500

def test_trade_records_final_exit():

    trade = Trade(
        symbol="NIFTY",
        entry_time=datetime.now(),
        entry_price=100,
        quantity=1,
    )

    trade.close(
        datetime.now(),
        120,
    )

    assert trade.events[-1].event == TradeEventType.FINAL_EXIT