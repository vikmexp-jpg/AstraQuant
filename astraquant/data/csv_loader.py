from pathlib import Path

import pandas as pd

from .schema import REQUIRED_COLUMNS


class CSVLoader:
    def __init__(self, path: str):
        self.path = Path(path)

    def load(self) -> pd.DataFrame:
        df = pd.read_csv(self.path)

        missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        df = df.sort_values("timestamp")

        return df.reset_index(drop=True)