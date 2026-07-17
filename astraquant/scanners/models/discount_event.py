from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class DiscountEvent:

    timestamp: datetime

    spot: float

    option: float

    intrinsic: float

    discount: float