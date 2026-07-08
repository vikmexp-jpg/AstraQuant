from dataclasses import dataclass
from .signal import SignalType

@dataclass
class StrategyResult:
    signal: SignalType
    reason: str
    expected_premium: float=0.0
    actual_premium: float=0.0
    discount: float=0.0
