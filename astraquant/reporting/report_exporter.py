from __future__ import annotations

from pathlib import Path
import csv

from astraquant.core.models import Trade
from .performance_report import PerformanceMetrics


class ReportExporter:
    """
    Export trade history and performance reports.
    """

    @staticmethod
    def export_trades(
        trades: list[Trade],
        output_dir: str | Path = "reports",
    ) -> None:

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        file = output_dir / "trades.csv"

        with file.open("w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                "Entry Time",
                "Exit Time",
                "Entry Price",
                "Exit Price",
                "Quantity",
                "PnL",
            ])

            for trade in trades:

                writer.writerow([
                    trade.entry_time,
                    trade.exit_time,
                    trade.entry_price,
                    trade.exit_price,
                    trade.quantity,
                    trade.pnl,
                ])

    @staticmethod
    def export_performance(
        metrics: PerformanceMetrics,
        output_dir: str | Path = "reports",
    ) -> None:

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        file = output_dir / "performance.csv"

        with file.open("w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(["Metric", "Value"])

            writer.writerow(["Total Trades", metrics.total_trades])
            writer.writerow(["Winning Trades", metrics.winning_trades])
            writer.writerow(["Losing Trades", metrics.losing_trades])
            writer.writerow(["Win Rate", metrics.win_rate])
            writer.writerow(["Total PnL", metrics.total_pnl])
            writer.writerow(["Average PnL", metrics.average_pnl])
            writer.writerow(["Peak Equity", metrics.peak_equity])
            writer.writerow(["Maximum Drawdown", metrics.maximum_drawdown])

    @staticmethod
    def print_summary(metrics: PerformanceMetrics) -> None:

        print("=" * 60)
        print("ASTRAQUANT BACKTEST REPORT")
        print("=" * 60)

        print(f"Total Trades      : {metrics.total_trades}")
        print(f"Winning Trades    : {metrics.winning_trades}")
        print(f"Losing Trades     : {metrics.losing_trades}")
        print(f"Win Rate          : {metrics.win_rate:.2f}%")
        print(f"Total PnL         : {metrics.total_pnl:.2f}")
        print(f"Average PnL       : {metrics.average_pnl:.2f}")
        print(f"Peak Equity       : {metrics.peak_equity:.2f}")
        print(f"Maximum Drawdown  : {metrics.maximum_drawdown:.2f}")

        print("=" * 60)