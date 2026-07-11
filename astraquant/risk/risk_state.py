from dataclasses import dataclass


@dataclass(slots=True)
class RiskState:
    trades_today: int = 0
    daily_pnl: float = 0.0
    consecutive_losses: int = 0