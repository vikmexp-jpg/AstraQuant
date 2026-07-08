from dataclasses import dataclass
from .candle import Candle

@dataclass(slots=True)
class StrategyContext:
    spot: Candle
    option: Candle
