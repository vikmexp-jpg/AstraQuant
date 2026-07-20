from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class OpportunitySummary:

    symbol: str

    option: str

    started_at: datetime
    ended_at: datetime

    duration_minutes: float

    start_discount: float
    peak_discount: float
    end_discount: float