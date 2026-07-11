from __future__ import annotations

from pathlib import Path

from astraquant.core.interfaces import IDataProvider
from astraquant.core.models import Candle

from .candle_factory import CandleFactory
from .csv_reader import CSVReader
from .csv_validator import CSVValidator


class CSVDataProvider(IDataProvider):
    """
    Historical CSV implementation of IDataProvider.
    """

    def __init__(self, csv_file: str | Path):
        self._csv_file = csv_file

    def candles(self) -> list[Candle]:

        dataframe = CSVReader.read(self._csv_file)

        CSVValidator.validate(dataframe)

        return CandleFactory.create(dataframe)