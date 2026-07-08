class PerformanceMetrics:

    @staticmethod
    def calculate(results):
        total = len(results)
        buys = sum(1 for r in results if r.signal.value == "BUY")
        return {
            "total_signals": total,
            "buy_signals": buys,
            "signal_rate": (buys / total * 100.0) if total else 0.0,
        }
