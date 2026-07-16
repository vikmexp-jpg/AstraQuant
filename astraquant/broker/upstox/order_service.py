from __future__ import annotations

from astraquant.broker import (
    BrokerOrder,
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

        if self.mode == TradingMode.PAPER:

            print("=" * 60)
            print("PAPER ORDER")
            print(order)
            print("=" * 60)

            return "PAPER-ORDER-001"

        raise NotImplementedError(
            "Live order placement will be implemented in AQ-010 Batch-3.4."
        )

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