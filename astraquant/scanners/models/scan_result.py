from __future__ import annotations

from dataclasses import dataclass

from .discount_event import DiscountEvent


@dataclass
class ScanResult:

    symbol: str

    option_symbol: str

    strike: int

    current_spot: float

    current_discount: float

    occurrences: int

    top_discounts: list[DiscountEvent]