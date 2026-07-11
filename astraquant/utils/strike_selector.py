from __future__ import annotations


class StrikeSelector:
    """
    Utility class for selecting option strikes.
    """

    @staticmethod
    def atm_strike(
        spot_price: float,
        interval: int = 50,
    ) -> int:
        """
        Return the nearest ATM strike.

        Example:
            24162 -> 24150
            24176 -> 24200
        """
        return round(spot_price / interval) * interval

    @staticmethod
    def strike(
        spot_price: float,
        offset: int,
        interval: int = 50,
    ) -> int:
        """
        Return strike after applying offset.

        Example:
            Spot = 24162
            ATM = 24150
            Offset = -500

            Result = 23650
        """
        atm = StrikeSelector.atm_strike(
            spot_price,
            interval,
        )

        return atm + offset