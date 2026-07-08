import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from astraquant.core.models.candle import Candle
from astraquant.strategies.didrs.context import StrategyContext
from astraquant.strategies.didrs.strategy import DIDRSStrategy

spot = Candle(
    timestamp=datetime.now(),
    open=24110,
    high=24120,
    low=24080,
    close=24090,
    volume=100000,
)

option = Candle(
    timestamp=datetime.now(),
    open=580,
    high=585,
    low=555,
    close=560,
    volume=10000,
)

ctx = StrategyContext(
    spot=spot,
    option=option,
)

strategy = DIDRSStrategy(
    threshold=20,
    itm_distance=500,
)

result = strategy.execute(ctx)

print(result)