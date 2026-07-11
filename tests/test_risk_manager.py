from astraquant.risk import RiskManager


def test_risk_state_updates():

    manager = RiskManager()

    assert manager.can_open_trade()

    manager.on_trade_open()

    assert manager.state.trades_today == 1

    manager.on_trade_close(-100)

    assert manager.state.daily_pnl == -100

    assert manager.state.consecutive_losses == 1

    manager.on_trade_close(50)

    assert manager.state.daily_pnl == -50

    assert manager.state.consecutive_losses == 0