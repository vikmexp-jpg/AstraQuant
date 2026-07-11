from __future__ import annotations

from datetime import datetime

import pandas as pd

from astraquant.core.models import Candle


class CandleFactory:
    """
    Converts a DataFrame into Candle objects.
    """

    @staticmethod
    def create(dataframe: pd.DataFrame) -> list[Candle]:
        candles: list[Candle] = []

        for _, row in dataframe.iterrows():
            candles.append(
                Candle(
                    timestamp=datetime.fromisoformat(str(row["timestamp"])),
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=int(row["volume"]),
                )
            )

        return candles