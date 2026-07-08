class PremiumCalculator:

    @staticmethod
    def expected(
        spot_close: float,
        strike: int,
    ) -> float:

        return spot_close - strike

    @staticmethod
    def discount(
        expected: float,
        actual: float,
    ) -> float:

        return expected - actual