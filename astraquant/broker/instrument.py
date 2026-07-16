from __future__ import annotations

from abc import ABC, abstractmethod

from .models import Instrument


class InstrumentService(ABC):
    """
    Abstract instrument lookup service.
    """

    @abstractmethod
    def find_option(
        self,
        symbol: str,
        strike: int,
        option_type: str,
    ) -> Instrument:
        """
        Return matching option instrument.
        """

    @abstractmethod
    def find_future(
        self,
        symbol: str,
        expiry: str,
    ) -> Instrument:
        """
        Return matching future instrument.
        """