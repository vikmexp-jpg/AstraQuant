from astraquant.strategies.didrs.strategy import DIDRSStrategy

class BacktestEngine:
    def __init__(self, strategy=None):
        self.strategy = strategy or DIDRSStrategy()
        self.results = []

    def run(self, contexts):
        self.results.clear()
        for ctx in contexts:
            self.results.append(self.strategy.execute(ctx))
        return self.results
