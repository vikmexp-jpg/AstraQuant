from astraquant.data.csv_loader import CSVLoader


def test_loader():
    loader = CSVLoader(
        "sample_data/nifty_spot_5m.csv"
    )

    df = loader.load()

    assert len(df) > 0