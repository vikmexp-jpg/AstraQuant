from dataclasses import dataclass
from .trade import Trade

@dataclass
class Position:
    trade: Trade
    target: float
    stop_loss: float
    is_open: bool=True
