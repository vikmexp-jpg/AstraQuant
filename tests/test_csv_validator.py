import pandas as pd

from astraquant.data import CSVValidator


def test_csv_validator():

    dataframe = pd.DataFrame(
        {
            "timestamp": [],
            "open": [],
            "high": [],
            "low": [],
            "close": [],
            "volume": [],
        }
    )

    CSVValidator.validate(dataframe)