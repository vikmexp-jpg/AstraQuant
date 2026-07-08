from dataclasses import dataclass

from astraquant.core.models.signal import SignalType


@dataclass
class StrategyResult:

    signal: SignalType

    strike: int

    expected: float

    actual: float

    discount: float

    reason: str