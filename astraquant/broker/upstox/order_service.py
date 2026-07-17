from __future__ import annotations

from astraquant.broker import (
    BrokerOrder,
    OrderType,
    TradingMode,
)


class UpstoxOrderService:
    """
    Handles order operations for Upstox.
    """

    def __init__(
        self,
        api_client,
        mode: TradingMode = TradingMode.PAPER,
    ):
        self.api_client = api_client
        self.mode = mode

    def place(
        self,
        order: BrokerOrder,
    ) -> str:

        self._validate(order)

        if self.mode == TradingMode.PAPER:
            return self._paper_place(order)

        return self._live_place(order)

    def cancel(
        self,
        order_id: str,
    ) -> None:

        raise NotImplementedError

    def status(
        self,
        order_id: str,
    ):

        raise NotImplementedError
    
    def _validate(
        self,
        order: BrokerOrder,
    ) -> None:

        if order.instrument is None:
            raise ValueError(
                "Instrument is required."
            )

        if order.quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

        if order.quantity % order.instrument.lot_size != 0:
            raise ValueError(
                f"Quantity must be a multiple of lot size ({order.instrument.lot_size})."
            )

        if (
            order.order_type == OrderType.LIMIT
            and order.price is None
        ):
            raise ValueError(
                "Limit order requires a price."
            )
        
    def _paper_place(
        self,
        order: BrokerOrder,
    ) -> str:

        print("=" * 60)
        print("PAPER ORDER")
        print(order)
        print("=" * 60)

        return "PAPER-ORDER-001"
    
    def _live_place(
        self,
        order: BrokerOrder,
    ) -> str:

        raise NotImplementedError(
            "Live order placement will be implemented after SDK validation."
        )