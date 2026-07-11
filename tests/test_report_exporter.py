from datetime import datetime
from pathlib import Path

from astraquant.core.models import Trade
from astraquant.reporting import (
    PerformanceReport,
    ReportExporter,
)


def test_export(tmp_path: Path):

    trade = Trade(
        symbol="NIFTY",
        entry_time=datetime.now(),
        entry_price=100,
        quantity=1,
    )

    trade.close(
        exit_time=datetime.now(),
        exit_price=110,
    )

    metrics = PerformanceReport.generate([trade])

    ReportExporter.export_trades(
        [trade],
        tmp_path,
    )

    ReportExporter.export_performance(
        metrics,
        tmp_path,
    )

    assert (tmp_path / "trades.csv").exists()
    assert (tmp_path / "performance.csv").exists()