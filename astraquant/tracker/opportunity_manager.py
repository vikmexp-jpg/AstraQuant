from __future__ import annotations

from astraquant.history.opportunity_history import OpportunityHistory
from astraquant.tracker.opportunity_status import OpportunityStatus
from astraquant.logger import logger

from .opportunity import Opportunity
from .opportunity_result import OpportunityResult
from .opportunity_state import OpportunityState


class OpportunityManager:

    def __init__(self):

        # One active opportunity per symbol
        self._active: dict[str, Opportunity] = {}

        # Completed opportunities
        self._completed: list[Opportunity] = []

        self.history = OpportunityHistory()

        # Opportunity ID generator
        self._next_id = 1

    def update(
        self,
        result: OpportunityResult,
    ) -> Opportunity:

        symbol = result.snapshot.symbol

        #
        # First opportunity
        #
        if symbol not in self._active:

            opportunity = Opportunity(
                id=self._next_id,
                symbol=symbol,
                started_at=result.snapshot.timestamp,
                last_updated=result.snapshot.timestamp,
                state=result.state,
                status=OpportunityStatus.ACTIVE,
                start_discount=result.current_discount,
                current_discount=result.current_discount,
                max_discount=result.current_discount,
                option=result.option_symbol,
            )

            self._next_id += 1
            self._active[symbol] = opportunity

            return opportunity

        #
        # Existing opportunity
        #
        opportunity = self._active[symbol]

        #
        # Previous opportunity has already ended.
        # Start a new lifecycle only if tracker reports NEW.
        #
        if (
            opportunity.status == OpportunityStatus.CLOSED
            and result.state == OpportunityState.NEW
        ):

            self._completed.append(opportunity)

            opportunity = Opportunity(
                id=self._next_id,
                symbol=symbol,
                started_at=result.snapshot.timestamp,
                last_updated=result.snapshot.timestamp,
                state=result.state,
                status=OpportunityStatus.ACTIVE,
                start_discount=result.current_discount,
                current_discount=result.current_discount,
                max_discount=result.current_discount,
                option=result.option_symbol,
            )

            self._next_id += 1
            self._active[symbol] = opportunity

            return opportunity

        #
        # Update existing opportunity
        #
        opportunity.last_updated = result.snapshot.timestamp
        opportunity.state = result.state
        opportunity.current_discount = result.current_discount

        #
        # Track highest discount reached
        #
        if result.current_discount > opportunity.max_discount:
            opportunity.max_discount = result.current_discount

        #
        # Close opportunity
        #
        if (
            opportunity.status == OpportunityStatus.ACTIVE
            and result.state == OpportunityState.RECOVERED
        ):

            opportunity.status = OpportunityStatus.CLOSED

            self.history.close(opportunity)

            print()
            print("=" * 80)
            print("OPPORTUNITY CLOSED")
            print("=" * 80)

            summary = self.history.repository.history[-1]

            print(f"Symbol       : {summary.symbol}")
            print(f"Option       : {summary.option}")
            print(f"Duration     : {summary.duration_minutes:.1f} min")
            print(f"Start        : {summary.start_discount:.2f}")
            print(f"Peak         : {summary.peak_discount:.2f}")
            print(f"End          : {summary.end_discount:.2f}")

            print("=" * 80)

        logger.info(
            "[MANAGER] %s State=%s Status=%s Max=%.2f Current=%.2f",
            opportunity.symbol,
            opportunity.state.value,
            opportunity.status.value,
            opportunity.max_discount,
            opportunity.current_discount,
        )

        return opportunity

    def active_opportunity(
        self,
        symbol: str,
    ) -> Opportunity | None:

        return self._active.get(symbol)

    @property
    def completed_opportunities(self) -> list[Opportunity]:

        return self._completed