from datetime import datetime

from astraquant.core.models import Trade
from astraquant.reporting import PerformanceReport


def trade(entry, exit_):

    t = Trade(
        symbol="NIFTY",
        entry_time=datetime.now(),
        entry_price=entry,
        quantity=1,
    )

    t.close(
        exit_time=datetime.now(),
        exit_price=exit_,
    )

    return t


def test_equity_curve():

    metrics = PerformanceReport.generate(
        [
            trade(100, 120),   # +20
            trade(100, 90),    # -10
            trade(100, 130),   # +30
        ]
    )

    assert metrics.total_pnl == 40

    assert metrics.equity_curve == [20, 10, 40]

    assert metrics.peak_equity == 40

    assert metrics.maximum_drawdown == 10