from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .discount_event import DiscountEvent


@dataclass
class ScanResult:

    symbol: str

    option_symbol: str

    strike: int

    timestamp: datetime

    spot: float

    option_price: float

    intrinsic: float

    discount: float

    occurrences: int

    top_discounts: list[DiscountEvent]