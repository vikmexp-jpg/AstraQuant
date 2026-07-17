from __future__ import annotations


class StrikeSelector:
    """
    Generic Strike Selector using floor-based anchor levels.
    """

    @staticmethod
    def anchor_strike(
        spot: float,
        offset: int,
    ) -> int:
        """
        Floor to the nearest anchor.

        Examples:

        offset = 500
            24081 -> 24000
            24563 -> 24500

        offset = 1000
            82962 -> 82000
            83580 -> 83000
        """

        return int(spot // offset) * offset

    @staticmethod
    def deep_itm_call(
        spot: float,
        offset: int,
    ) -> int:
        """
        One anchor below.
        """

        return (
            StrikeSelector.anchor_strike(
                spot,
                offset,
            )
            - offset
        )

    @staticmethod
    def deep_itm_put(
        spot: float,
        offset: int,
    ) -> int:
        """
        One anchor above.
        """

        return (
            StrikeSelector.anchor_strike(
                spot,
                offset,
            )
            + offset
        )