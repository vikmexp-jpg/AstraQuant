from __future__ import annotations

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
        # Ignore symbols that have no intrinsic opportunity.
        # (Example: Deep ITM CE trading above intrinsic value.)
        #
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
        if lifecycle.status == OpportunityStatus.CLOSED:

            self.tracker.reset(
                symbol,
            )
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
        # Notify only BUY signals.
        # Lifecycle is still updated for HOLD/RECOVERED.
        #
        if signal.action == "BUY":
            AlertEngine.notify(alert)

        return lifecycle