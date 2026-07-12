from __future__ import annotations

from astraquant.core.models import Candle


class VolumeAnalyzer:
    """
    Utility functions for option volume analysis.
    """

    @staticmethod
    def average_volume(
        candles: list[Candle],
    ) -> float:
        """
        Return the average volume.

        Returns 0 if the list is empty.
        """

        if not candles:
            return 0.0

        total = sum(
            candle.volume
            for candle in candles
        )

        return total / len(candles)

    @staticmethod
    def is_volume_confirmed(
        history: list[Candle],
        current: Candle,
    ) -> bool:
        """
        Current candle volume must exceed
        the average of the previous candles.
        """

        average = VolumeAnalyzer.average_volume(
            history,
        )

        return current.volume > average