class BacktestReport:
    @staticmethod
    def summarize(results):
        total = len(results)
        buys = sum(1 for r in results if r.signal.value == "BUY")
        return {
            "total_signals": total,
            "buy_signals": buys,
            "no_signals": total - buys,
        }
