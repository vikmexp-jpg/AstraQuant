from __future__ import annotations

import os

from dotenv import load_dotenv

import upstox_client
from upstox_client.rest import ApiException

from astraquant.broker.models import TradingMode
from .instrument_service import UpstoxInstrumentService
from .order_service import UpstoxOrderService

from astraquant.broker import (
    Broker,
    BrokerOrder,
    BrokerPosition,
    MarketQuote,
)


class UpstoxBroker(Broker):
    """
    Upstox broker implementation.
    """

    def __init__(self) -> None:

        load_dotenv()

        token = os.getenv("UPSTOX_ACCESS_TOKEN")

        if not token:
            raise RuntimeError(
                "UPSTOX_ACCESS_TOKEN missing."
            )

        configuration = upstox_client.Configuration()
        configuration.access_token = token

        self.api_client = upstox_client.ApiClient(
            configuration
        )
        self.order_service = UpstoxOrderService(
            self.api_client,
            TradingMode.PAPER,
        )

        self.instrument_service = UpstoxInstrumentService(
            self.api_client,
        )

        self.user_api = upstox_client.UserApi(
            self.api_client
        )

        self.market_api = upstox_client.MarketQuoteApi(
            self.api_client
        )

    def connect(self) -> None:

        self.user_api.get_profile(
            api_version="2.0",
        )

    def get_quote(
        self,
        instrument: str,
    ) -> MarketQuote:
        """
        Fetch latest market quote from Upstox.
        """

        response = self.market_api.get_full_market_quote(
            symbol=instrument,
            api_version="2.0",
        )

        if not response.data:
            raise RuntimeError(
                f"No market data returned for '{instrument}'."
            )

        # Upstox uses keys like:
        # "NSE_INDEX:Nifty 50"
        # instead of the requested
        # "NSE_INDEX|Nifty 50"
        quote = next(iter(response.data.values()))

        return MarketQuote(
            instrument=quote.instrument_token,
            ltp=quote.last_price,
        )

    def place_order(
        self,
        order: BrokerOrder,
    ) -> str:

        raise NotImplementedError(
            "Order placement in Batch-3."
        )

    def positions(
        self,
    ) -> list[BrokerPosition]:

        raise NotImplementedError(
            "Positions in Batch-3."
        )
    @property
    def instruments(self) -> UpstoxInstrumentService:
        """
        Access instrument lookup service.
        """
        return self.instrument_service
    
    @property
    def orders(self) -> UpstoxOrderService:
        return self.order_service