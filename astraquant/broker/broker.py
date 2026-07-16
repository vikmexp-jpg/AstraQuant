from __future__ import annotations

from abc import ABC, abstractmethod

from .models import (
    BrokerOrder,
    BrokerPosition,
    MarketQuote,
)


class Broker(ABC):
    """
    Base interface for all brokers.
    """

    @abstractmethod
    def connect(self) -> None:
        """Connect to broker."""

    @abstractmethod
    def get_quote(
        self,
        instrument: str,
    ) -> MarketQuote:
        """Return latest market quote."""

    @abstractmethod
    def place_order(
        self,
        order: BrokerOrder,
    ) -> str:
        """Place an order."""

    @abstractmethod
    def positions(
        self,
    ) -> list[BrokerPosition]:
        """Return open positions."""