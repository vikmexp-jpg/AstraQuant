from astraquant.engine import BacktestEngine


def test_backtest_runs():

    engine = BacktestEngine(
        "sample_data/spot.csv",
        "sample_data/option.csv",
    )

    trades = engine.run()

    assert isinstance(trades, list)

    assert engine.total_signals >= 0

    assert engine.total_trades >= 0

    assert engine.total_signals >= engine.total_trades