from __future__ import annotations

from astraquant.logger import logger
from astraquant.alerts.alert import Alert
from astraquant.alerts.alert_engine import AlertEngine
from astraquant.scanners.discount_scanner import DiscountScanner
from astraquant.signals.didrs_signal import DidrsSignal
from astraquant.tracker.opportunity_status import OpportunityStatus
from astraquant.tracker import (
    DiscountSnapshot,
    DiscountTracker,
    OpportunityManager,
)


class DidrsEngine:

    def __init__(self, broker):

        self.scanner = DiscountScanner(broker)
        self.tracker = DiscountTracker()
        self.manager = OpportunityManager()

    def run(
        self,
        symbol: str,
        threshold: float,
    ):

        result = self.scanner.scan(
            symbol=symbol,
            option_type="CE",
            interval="5minute",
            threshold=threshold,
        )

        if result is None:
            return None

        #
        # Existing opportunity
        #
        active = self.manager.active_opportunity(symbol)

        #
        # Ignore discounts below entry threshold
        # only when there is NO active opportunity.
        #
        print(f"[{symbol}] Discount = {result.discount:.2f}")
        
        if (
            result.discount < threshold
            and (
                active is None
                or active.status == OpportunityStatus.CLOSED
            )
        ):

            logger.info(
                "[%s] No Opportunity | Discount=%.2f Threshold=%.2f",
                symbol,
                result.discount,
                threshold,
            )

            return None

        #
        # Current market snapshot
        #
        snapshot = DiscountSnapshot(
            symbol=result.symbol,
            timestamp=result.timestamp,
            spot=result.spot,
            option_price=result.option_price,
            intrinsic=result.intrinsic,
            discount=result.discount,
            option_symbol=result.option_symbol,
        )

        #
        # Opportunity lifecycle
        #
        opportunity_result = self.tracker.update(snapshot)

        lifecycle = self.manager.update(
            opportunity_result
        )

        #
        # Tracker reset after opportunity closes.
        #
        if lifecycle.status == OpportunityStatus.CLOSED:

            self.tracker.reset(symbol)

        #
        # Trading signal
        #
        signal = DidrsSignal.generate(
            current_discount=result.discount,
            threshold=threshold,
        )

        #
        # Alert
        #
        alert = Alert(
            symbol=result.symbol,
            option=result.option_symbol,
            signal=signal.action,
            current_discount=result.discount,
            top_discount=result.top_discounts,
            opportunity=lifecycle,
        )

        #
        # Notify BUY signals only.
        #
        if signal.action == "BUY":
            AlertEngine.notify(alert)

        return lifecycle