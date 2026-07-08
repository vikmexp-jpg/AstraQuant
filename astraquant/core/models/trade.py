from dataclasses import dataclass
from datetime import datetime

@dataclass
class Trade:
    symbol:str
    entry_price:float
    quantity:int
    entry_time:datetime
    exit_price:float|None=None
    exit_time:datetime|None=None
    pnl:float=0.0
