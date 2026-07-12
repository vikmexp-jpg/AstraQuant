from __future__ import annotations

from astraquant.core.models import (
    Candle,
    Signal,
    SignalType,
)
from typing import TYPE_CHECKING
from astraquant.utils import VolumeAnalyzer

if TYPE_CHECKING:
    from astraquant.engine import SynchronizedCandle


class DIDRSStrategy:
    """
    Discount Intraday Deep ITM Reversal Strategy.
    """

    def __init__(
        self,
        minimum_discount: float = 20.0,
        minimum_volume: int = 1,
    ):

        self.minimum_discount = minimum_discount
        self.minimum_volume = minimum_volume

    def evaluate(
            self,
            context: SynchronizedCandle,
            expected_premium: float,
            strike: int,
            previous_option_candles: list[Candle],
        ) -> Signal | None:

        option = context.option
        spot = context.spot

        discount = expected_premium - option.close

        if not spot.is_red:
            return None

        if not option.is_red:
            return None

        if discount < self.minimum_discount:
            return None

        if len(previous_option_candles) < 5:
            return None

        if not VolumeAnalyzer.is_volume_confirmed(
            previous_option_candles,
            option,
        ):
            return None

        return Signal(
            timestamp=spot.timestamp,
            signal=SignalType.BUY,
            price=option.close,
            strategy="DIDRS",
            reason=f"Discount={discount:.2f}, Strike={strike}",
        )