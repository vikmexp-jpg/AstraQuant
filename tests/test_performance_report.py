from datetime import datetime

from astraquant.core.models import Trade
from astraquant.reporting import PerformanceReport


def test_performance_report():

    trade1 = Trade(
        symbol="NIFTY",
        entry_time=datetime.now(),
        entry_price=100,
        quantity=1,
    )
    trade1.close(
        exit_time=datetime.now(),
        exit_price=120,
    )

    trade2 = Trade(
        symbol="NIFTY",
        entry_time=datetime.now(),
        entry_price=100,
        quantity=1,
    )
    trade2.close(
        exit_time=datetime.now(),
        exit_price=90,
    )

    metrics = PerformanceReport.generate(
        [trade1, trade2]
    )

    assert metrics.total_trades == 2
    assert metrics.winning_trades == 1
    assert metrics.losing_trades == 1
    assert metrics.total_pnl == 10
    assert metrics.win_rate == 50.0