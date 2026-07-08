from astraquant.backtest.backtest_engine import BacktestEngine
from astraquant.backtest.report import BacktestReport

class BacktestRunner:
    def __init__(self, strategy):
        self.engine = BacktestEngine(strategy)

    def run(self, contexts):
        results = self.engine.run(contexts)
        summary = BacktestReport.summarize(results)
        return results, summary
