from astraquant.data import CSVDataProvider


def test_csv_provider():

    provider = CSVDataProvider(
        "sample_data/sample.csv"
    )

    candles = provider.candles()

    assert len(candles) == 3

    assert candles[0].open == 100

    assert candles[2].close == 107