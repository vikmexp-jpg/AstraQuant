from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class DiscountEvent:

    time: datetime
    spot: float
    option: float
    intrinsic: float
    discount: float


@dataclass
class ScanResult:

    symbol: str
    option_symbol: str

    strike: int

    current_spot: float
    current_discount: float

    occurrences: int

    top_discounts: list[DiscountEvent]