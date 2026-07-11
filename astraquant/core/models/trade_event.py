from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TradeEventType(Enum):
    ENTRY = "ENTRY"
    TARGET_50 = "TARGET_50"
    BREAK_EVEN = "BREAK_EVEN"
    TRAILING_UPDATE = "TRAILING_UPDATE"
    FINAL_EXIT = "FINAL_EXIT"


@dataclass(slots=True)
class TradeEvent:
    timestamp: datetime
    event: TradeEventType
    price: float | None = None
    quantity: int | None = None
    note: str = ""