from __future__ import annotations

from dataclasses import dataclass

from astraquant.core.models import Trade


@dataclass(slots=True)
class PerformanceMetrics:
    total_trades: int
    winning_trades: int
    losing_trades: int
    win_rate: float
    total_pnl: float
    average_pnl: float
    equity_curve: list[float]
    peak_equity: float
    maximum_drawdown: float


class PerformanceReport:
    """
    Calculates performance statistics from completed trades.
    """

    @staticmethod
    def generate(trades: list[Trade]) -> PerformanceMetrics:

        completed = [
            trade
            for trade in trades
            if trade.exit_price is not None
        ]

        total = len(completed)

        winners = sum(
            1
            for trade in completed
            if trade.pnl > 0
        )

        losers = total - winners

        total_pnl = sum(
            trade.pnl
            for trade in completed
        )

        average = (
            total_pnl / total
            if total
            else 0.0
        )

        win_rate = (
            winners / total * 100
            if total
            else 0.0
        )

        equity_curve = []

        equity = 0.0

        peak = 0.0

        max_drawdown = 0.0

        for trade in completed:

            equity += trade.pnl

            equity_curve.append(equity)

            if equity > peak:
                peak = equity

            drawdown = peak - equity

            if drawdown > max_drawdown:
                max_drawdown = drawdown

        return PerformanceMetrics(
            total_trades=total,
            winning_trades=winners,
            losing_trades=losers,
            win_rate=win_rate,
            total_pnl=total_pnl,
            average_pnl=average,
            equity_curve=equity_curve,
            peak_equity=peak,
            maximum_drawdown=max_drawdown,
        )