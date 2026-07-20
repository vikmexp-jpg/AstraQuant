from __future__ import annotations

from .discount_snapshot import DiscountSnapshot
from .opportunity_result import OpportunityResult
from .opportunity_state import OpportunityState
from astraquant.logger import logger


class DiscountTracker:

    def __init__(
        self,
        stable_tolerance: float = 0.5,
        improvement_step: float = 2.0,
        recovered_threshold: float = 2.0,
    ):

        self._previous: dict[str, DiscountSnapshot] = {}

        self.stable_tolerance = stable_tolerance
        self.improvement_step = improvement_step
        self.recovered_threshold = recovered_threshold

    def update(
        self,
        snapshot: DiscountSnapshot,
    ) -> OpportunityResult:

        previous = self._previous.get(snapshot.symbol)

        logger.info(
            "[TRACKER] %s Previous=%s Current=%.2f",
            snapshot.symbol,
            (
                "-"
                if previous is None
                else f"{previous.discount:.2f}"
            ),
            snapshot.discount,
        )

        self._previous[snapshot.symbol] = snapshot

        #
        # First opportunity
        #
        if previous is None:

            return OpportunityResult(
                state=OpportunityState.NEW,
                previous_discount=None,
                current_discount=snapshot.discount,
                change=0.0,
                snapshot=snapshot,
                option_symbol=snapshot.option_symbol,
            )

        change = snapshot.discount - previous.discount

        #
        # Opportunity recovered
        #
        if snapshot.discount <= self.recovered_threshold:

            return OpportunityResult(
                state=OpportunityState.RECOVERED,
                previous_discount=previous.discount,
                current_discount=snapshot.discount,
                change=change,
                snapshot=snapshot,
                option_symbol=snapshot.option_symbol,
            )

        #
        # Opportunity improving
        #
        if change >= self.improvement_step:

            return OpportunityResult(
                state=OpportunityState.IMPROVING,
                previous_discount=previous.discount,
                current_discount=snapshot.discount,
                change=change,
                snapshot=snapshot,
                option_symbol=snapshot.option_symbol,
            )

        #
        # Opportunity weakening
        #
        if change <= -self.improvement_step:

            return OpportunityResult(
                state=OpportunityState.WEAKENING,
                previous_discount=previous.discount,
                current_discount=snapshot.discount,
                change=change,
                snapshot=snapshot,
                option_symbol=snapshot.option_symbol,
            )

        #
        # Stable
        #
        return OpportunityResult(
            state=OpportunityState.STABLE,
            previous_discount=previous.discount,
            current_discount=snapshot.discount,
            change=change,
            snapshot=snapshot,
            option_symbol=snapshot.option_symbol,
        )
    
    def reset(self, symbol: str) -> None:

        print(f"[TRACKER] RESET -> {symbol}")

        self._previous.pop(symbol, None)