from __future__ import annotations

from dataclasses import dataclass

from .candle import Candle
from dataclasses import field


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
    previous_option_candles: list[Candle] = field(default_factory=list)