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

        return PerformanceMetrics(
            total_trades=total,
            winning_trades=winners,
            losing_trades=losers,
            win_rate=win_rate,
            total_pnl=total_pnl,
            average_pnl=average,
        )