from __future__ import annotations

from dataclasses import dataclass

from astraquant.core.models import Candle


@dataclass(frozen=True, slots=True)
class SynchronizedCandle:
    """
    Pair of spot and option candles having the same timestamp.
    """
    spot: Candle
    option: Candle


class CandleSynchronizer:
    """
    Synchronizes spot and option candles using timestamp.
    """

    @staticmethod
    def synchronize(
        spot_candles: list[Candle],
        option_candles: list[Candle],
    ) -> list[SynchronizedCandle]:

        option_map = {
            candle.timestamp: candle
            for candle in option_candles
        }

        synchronized: list[SynchronizedCandle] = []

        for spot in spot_candles:

            option = option_map.get(spot.timestamp)

            if option is None:
                continue

            synchronized.append(
                SynchronizedCandle(
                    spot=spot,
                    option=option,
                )
            )

        return synchronized