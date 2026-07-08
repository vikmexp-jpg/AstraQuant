import pandas as pd


class CandleSynchronizer:

    def synchronize(
        self,
        spot: pd.DataFrame,
        option: pd.DataFrame,
    ) -> pd.DataFrame:

        return pd.merge(
            spot,
            option,
            on="timestamp",
            suffixes=("_spot", "_option"),
            how="inner",
        )