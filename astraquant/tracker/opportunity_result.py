from dataclasses import dataclass

from .discount_snapshot import DiscountSnapshot
from .opportunity_state import OpportunityState


@dataclass(slots=True)
class OpportunityResult:

    snapshot: DiscountSnapshot

    state: OpportunityState

    previous_discount: float | None
    current_discount: float

    change: float

    option_symbol: str