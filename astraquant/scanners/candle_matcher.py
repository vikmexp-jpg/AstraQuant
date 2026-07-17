from __future__ import annotations

from astraquant.core.models import Candle


class CandleMatcher:

    @staticmethod
    def match(
        spot: list[Candle],
        option: list[Candle],
    ) -> list[tuple[Candle, Candle]]:

        option_map = {
            c.timestamp: c
            for c in option
        }

        result = []

        for s in spot:

            o = option_map.get(s.timestamp)

            if o is not None:
                result.append((s, o))

        return result