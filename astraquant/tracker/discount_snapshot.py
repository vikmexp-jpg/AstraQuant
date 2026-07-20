from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class DiscountSnapshot:

    symbol: str
    timestamp: datetime

    spot: float
    option_price: float
    intrinsic: float

    discount: float

    option_symbol: str