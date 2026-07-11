from __future__ import annotations

from pathlib import Path

import pandas as pd


class CSVReader:
    """
    Reads CSV files into a pandas DataFrame.
    """

    @staticmethod
    def read(file_path: str | Path) -> pd.DataFrame:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)

        return pd.read_csv(path)