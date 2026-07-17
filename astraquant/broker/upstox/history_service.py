from __future__ import annotations

from datetime import datetime

from astraquant.core.models import Candle
from astraquant.data.candle_aggregator import CandleAggregator


class UpstoxHistoryService:
    """
    Historical / Intraday candle service.
    """

    def __init__(self, history_api):

        self.history_api = history_api

    def get_intraday_candles(
        self,
        instrument_key: str,
        interval: str = "1minute",
    ) -> list[Candle]:

        api_interval = interval
        aggregation = None

        if interval == "5minute":
            api_interval = "1minute"
            aggregation = 5

        response = self.history_api.get_intra_day_candle_data(
            instrument_key=instrument_key,
            interval=api_interval,
            api_version="2.0",
        )
        print("=" * 80)
        print(response)
        print("=" * 80)

        candles = []

        for item in response.data.candles:
            candles.append(
                Candle(
                    timestamp=datetime.fromisoformat(item[0]),
                    open=float(item[1]),
                    high=float(item[2]),
                    low=float(item[3]),
                    close=float(item[4]),
                    volume=int(item[5]),
                )
            )

        # Upstox returns latest candle first.
        candles.reverse()

        if aggregation is not None:
            candles = CandleAggregator.aggregate(
                candles,
                aggregation,
            )

        return candles
    


    def get_historical_candles(
        self,
        instrument_key: str,
        to_date: str,
        start_datetime: datetime | None = None,
        end_datetime: datetime | None = None,
    ) -> list[Candle]:

        response = self.history_api.get_historical_candle_data(
            instrument_key=instrument_key,
            interval="1minute",
            to_date=to_date,
            api_version="2.0",
        )

        candles = []

        for item in response.data.candles:

            candle = Candle(
                timestamp=datetime.fromisoformat(item[0]),
                open=float(item[1]),
                high=float(item[2]),
                low=float(item[3]),
                close=float(item[4]),
                volume=int(item[5]),
            )

            if start_datetime is not None:
                if candle.timestamp < start_datetime:
                    continue

            if end_datetime is not None:
                if candle.timestamp > end_datetime:
                    continue

            candles.append(candle)

        candles.reverse()

        return candles