from astraquant.engine import BacktestEngine


def test_backtest_pipeline():

    engine = BacktestEngine(
        "sample_data/spot.csv",
        "sample_data/option.csv",
    )

    trades = engine.run()

    assert trades is not None

    assert engine.total_signals >= engine.total_trades

    assert isinstance(trades, list)