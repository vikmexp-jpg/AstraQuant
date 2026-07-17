from __future__ import annotations

from astraquant.core.models import Candle


class CandleAggregator:
    """
    Aggregates smaller timeframe candles
    into larger timeframe candles.
    """

    @staticmethod
    def aggregate(
        candles: list[Candle],
        interval: int,
    ) -> list[Candle]:

        if interval <= 1:
            return candles

        aggregated = []

        for i in range(0, len(candles), interval):

            batch = candles[i:i + interval]

            if len(batch) < interval:
                break

            aggregated.append(
                Candle(
                    timestamp=batch[0].timestamp,
                    open=batch[0].open,
                    high=max(c.high for c in batch),
                    low=min(c.low for c in batch),
                    close=batch[-1].close,
                    volume=sum(c.volume for c in batch),
                )
            )

        return aggregated