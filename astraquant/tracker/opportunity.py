from dataclasses import dataclass
from datetime import datetime

from .opportunity_state import OpportunityState
from .opportunity_status import OpportunityStatus


@dataclass(slots=True)
class Opportunity:

    id: int
    
    symbol: str

    started_at: datetime
    last_updated: datetime

    state: OpportunityState
    status: OpportunityStatus

    start_discount: float
    current_discount: float
    max_discount: float

    option: str