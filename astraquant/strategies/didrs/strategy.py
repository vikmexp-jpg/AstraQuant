from astraquant.core.models.signal import SignalType

from .context import StrategyContext
from .premium import PremiumCalculator
from .result import StrategyResult
from .strike_selector import StrikeSelector
from .validator import CandleValidator


class DIDRSStrategy:

    def __init__(

        self,

        threshold=20,

        itm_distance=500,

    ):

        self.threshold = threshold

        self.selector = StrikeSelector(
            itm_distance
        )

    def execute(

        self,

        ctx: StrategyContext,

    ) -> StrategyResult:

        if not CandleValidator.is_red(
            ctx.spot
        ):

            return StrategyResult(

                SignalType.NONE,

                0,

                0,

                0,

                0,

                "Spot candle is not red",

            )

        if not CandleValidator.is_red(
            ctx.option
        ):

            return StrategyResult(

                SignalType.NONE,

                0,

                0,

                0,

                0,

                "Option candle is not red",

            )

        strike = self.selector.get_strike(
            ctx.spot.close
        )

        expected = PremiumCalculator.expected(

            ctx.spot.close,

            strike,

        )

        discount = PremiumCalculator.discount(

            expected,

            ctx.option.close,

        )

        if discount >= self.threshold:

            return StrategyResult(

                SignalType.BUY,

                strike,

                expected,

                ctx.option.close,

                discount,

                "Discount detected",

            )

        return StrategyResult(

            SignalType.NONE,

            strike,

            expected,

            ctx.option.close,

            discount,

            "Discount below threshold",

        )