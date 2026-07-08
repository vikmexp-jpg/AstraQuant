import pandas as pd

class CandleSynchronizer:
    def synchronize(self,spot_df,option_df):
        return pd.merge(
            spot_df,
            option_df,
            on="timestamp",
            suffixes=("_spot","_option"),
            how="inner",
        )
