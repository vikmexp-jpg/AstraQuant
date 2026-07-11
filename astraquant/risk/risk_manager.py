from .risk_state import RiskState


class RiskManager:
    """
    Controls whether new trades are allowed.
    """

    def __init__(self):

        self.state = RiskState()

    def can_open_trade(self) -> bool:
        """
        Foundation implementation.

        More rules will be added in Batch-2.
        """
        return True

    def on_trade_open(self):

        self.state.trades_today += 1

    def on_trade_close(self, pnl: float):

        self.state.daily_pnl += pnl

        if pnl < 0:
            self.state.consecutive_losses += 1
        else:
            self.state.consecutive_losses = 0