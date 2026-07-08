from dataclasses import dataclass
from enum import Enum

class SignalType(Enum):
    BUY='BUY'
    SELL='SELL'
    EXIT='EXIT'
    NONE='NONE'

@dataclass
class StrategySignal:
    signal: SignalType
    reason: str=''
