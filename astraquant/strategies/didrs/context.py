from dataclasses import dataclass

from astraquant.core.models.candle import Candle


@dataclass(slots=True)
class StrategyContext:

    spot: Candle

    option: Candle