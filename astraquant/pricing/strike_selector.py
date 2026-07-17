from __future__ import annotations


class StrikeSelector:
    """
    Strike selection based on AstraQuant strategy.
    Valid anchor strikes:
    23000, 23500, 24000, 24500...
    """

    @staticmethod
    def nearest_500(
        spot: float,
    ) -> int:
        """
        Floor to nearest 500.

        Examples:
        24081 -> 24000
        24399 -> 24000
        24501 -> 24500
        """

        return int(spot // 500) * 500

    @staticmethod
    def deep_itm_call(
        spot: float,
        levels: int = 1,
    ) -> int:
        """
        Deep ITM Call.

        levels=1 -> current 500 strike
        levels=2 -> one level below
        """

        return (
            StrikeSelector.nearest_500(spot)
            - (levels - 1) * 500
        )

    @staticmethod
    def deep_itm_put(
        spot: float,
        levels: int = 1,
    ) -> int:
        """
        Deep ITM Put.

        levels=1 -> current 500 strike
        levels=2 -> one level above
        """

        return (
            StrikeSelector.nearest_500(spot)
            + (levels - 1) * 500
        )