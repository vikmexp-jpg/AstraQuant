from astraquant.core.models.signal import SignalType
from astraquant.core.models.strategy_result import StrategyResult
from .strike_selector import StrikeSelector
from .premium import PremiumCalculator
from .validator import CandleValidator

class DIDRSStrategy:
    def __init__(self,threshold=20,itm_distance=500):
        self.threshold=threshold
        self.selector=StrikeSelector(itm_distance)

    def execute(self,context):
        if not CandleValidator.is_red(context.spot):
            return StrategyResult(signal=SignalType.NONE,reason="Spot candle is not red")
        if not CandleValidator.is_red(context.option):
            return StrategyResult(signal=SignalType.NONE,reason="Option candle is not red")

        strike=self.selector.get_strike(context.spot.close)
        expected=PremiumCalculator.expected_premium(context.spot.close,strike)
        actual=context.option.close
        discount=PremiumCalculator.discount(expected,actual)

        if discount>=self.threshold:
            return StrategyResult(
                signal=SignalType.BUY,
                reason="Discount detected",
                expected_premium=expected,
                actual_premium=actual,
                discount=discount
            )

        return StrategyResult(
            signal=SignalType.NONE,
            reason="Discount below threshold",
            expected_premium=expected,
            actual_premium=actual,
            discount=discount
        )
