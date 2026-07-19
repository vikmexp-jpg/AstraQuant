from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from astraquant.scanners.models.discount_event import DiscountEvent


@dataclass
class Alert:

    symbol: str
    option: str
    top_discount: list[DiscountEvent]
    current_discount: float
    signal: str