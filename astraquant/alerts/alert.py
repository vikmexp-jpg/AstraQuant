from dataclasses import dataclass

from astraquant.scanners.models.discount_event import DiscountEvent
from astraquant.tracker.opportunity import Opportunity


@dataclass(slots=True)
class Alert:

    symbol: str
    option: str
    signal: str

    current_discount: float

    top_discount: list[DiscountEvent]

    opportunity: Opportunity