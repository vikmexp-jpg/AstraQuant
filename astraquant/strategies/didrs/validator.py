class CandleValidator:

    @staticmethod
    def is_red(candle):

        return candle.close < candle.open