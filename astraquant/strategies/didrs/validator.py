class CandleValidator:
    @staticmethod
    def is_red(candle)->bool:
        return candle.close<candle.open
