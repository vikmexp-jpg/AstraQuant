from __future__ import annotations

from dataclasses import dataclass

from .candle import Candle


@dataclass(frozen=True, slots=True)
class StrategyContext:
    """
    Complete market context supplied to a strategy.
    """

    spot: Candle

    option: Candle

    strike: int

    expected_premium: float

    discount: float