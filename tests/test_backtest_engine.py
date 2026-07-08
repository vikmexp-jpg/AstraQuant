from datetime import datetime
from astraquant.backtest.backtest_engine import BacktestEngine
from astraquant.core.models.candle import Candle
from astraquant.core.models.strategy_context import StrategyContext

def test_engine_runs():
    spot = Candle(datetime.now(),24110,24120,24080,24090,1000)
    option = Candle(datetime.now(),580,585,555,560,100)
    ctx = StrategyContext(spot=spot, option=option)
    engine = BacktestEngine()
    results = engine.run([ctx])
    assert len(results) == 1
