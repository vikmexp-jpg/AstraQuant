from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from astraquant.core.models import Candle


class IDataProvider(ABC):
    """
    Interface for market data providers.
    """

    @abstractmethod
    def candles(self) -> Iterable[Candle]:
        """
        Return an iterable of Candle objects.
        """
        raise NotImplementedError