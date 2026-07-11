from astraquant.data import CSVReader


def test_csv_reader():

    dataframe = CSVReader.read(
        "sample_data/sample.csv"
    )

    assert len(dataframe) == 3

    assert list(dataframe.columns) == [
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]