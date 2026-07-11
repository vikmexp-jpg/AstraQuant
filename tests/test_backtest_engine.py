from astraquant.engine import BacktestEngine


def test_backtest_runs():

    engine = BacktestEngine(
        "sample_data/spot.csv",
        "sample_data/option.csv",
    )

    signals = engine.run()

    assert signals >= 0