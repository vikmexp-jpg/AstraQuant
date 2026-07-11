from __future__ import annotations

from astraquant.core.models import Candle


class PremiumCalculator:
    """
    Calculates expected premium.

    NOTE:
    This is a placeholder implementation.
    A real premium model will replace it when
    live option pricing is introduced.
    """

    @staticmethod
    def expected_premium(
        spot: Candle,
        strike: int,
    ) -> float:

        intrinsic = max(
            spot.close - strike,
            0,
        )

        return intrinsic + 20