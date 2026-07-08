from datetime import datetime
from astraquant.core.models.candle import Candle
from astraquant.core.models.strategy_context import StrategyContext
from astraquant.core.models.signal import SignalType
from astraquant.strategies.didrs.strategy import DIDRSStrategy

def test_discount_buy_signal():
    spot=Candle(datetime.now(),24110,24120,24080,24090,1000)
    option=Candle(datetime.now(),580,585,555,560,500)
    result=DIDRSStrategy(threshold=20).execute(
        StrategyContext(spot=spot,option=option)
    )
    assert result.signal==SignalType.BUY
    assert result.discount==30
