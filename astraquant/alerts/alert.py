from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Alert:

    symbol: str
    option: str

    timestamp: datetime

    discount: float

    signal: str