class TradeManager:
    def __init__(self, target_points=30, stop_loss_points=20):
        self.target_points = target_points
        self.stop_loss_points = stop_loss_points

    def evaluate(self, entry_price, current_price):
        pnl = current_price - entry_price
        if pnl >= self.target_points:
            return "TARGET", pnl
        if pnl <= -self.stop_loss_points:
            return "STOPLOSS", pnl
        return "OPEN", pnl
