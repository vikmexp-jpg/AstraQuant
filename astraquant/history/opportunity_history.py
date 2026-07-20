from .history_repository import HistoryRepository
from .opportunity_summary import OpportunitySummary


class OpportunityHistory:

    def __init__(self):

        self.repository = HistoryRepository()

    def close(self, opportunity):

        summary = OpportunitySummary(
            symbol=opportunity.symbol,
            option=opportunity.option,

            started_at=opportunity.started_at,
            ended_at=opportunity.last_updated,

            duration_minutes=(
                opportunity.last_updated
                - opportunity.started_at
            ).total_seconds() / 60,

            start_discount=opportunity.start_discount,
            peak_discount=opportunity.max_discount,
            end_discount=opportunity.current_discount,
        )

        self.repository.add(summary)