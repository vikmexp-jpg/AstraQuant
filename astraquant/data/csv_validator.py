from __future__ import annotations

import pandas as pd


class CSVValidator:

    REQUIRED_COLUMNS = (
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
    )

    @classmethod
    def validate(cls, dataframe: pd.DataFrame) -> None:

        missing = [
            column
            for column in cls.REQUIRED_COLUMNS
            if column not in dataframe.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required columns: {', '.join(missing)}"
            )