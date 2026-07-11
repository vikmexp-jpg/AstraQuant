from datetime import datetime

from astraquant.core.models import Trade, TradeStatus


def test_trade_close():

    trade = Trade(
        symbol="NIFTY",
        entry_time=datetime.now(),
        entry_price=100,
        quantity=10,
    )

    trade.close(
        exit_time=datetime.now(),
        exit_price=110,
    )

    assert trade.status == TradeStatus.CLOSED

    assert trade.pnl == 100