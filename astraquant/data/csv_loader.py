from pathlib import Path
import pandas as pd
from .schema import REQUIRED_COLUMNS

class CSVLoader:
    def load(self,path):
        df=pd.read_csv(Path(path))
        missing=[c for c in REQUIRED_COLUMNS if c not in df.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")
        df["timestamp"]=pd.to_datetime(df["timestamp"])
        return df.sort_values("timestamp").reset_index(drop=True)
