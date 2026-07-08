from astraquant.data.csv_loader import CSVLoader

def test_loader():
    df=CSVLoader().load("sample_data/nifty_spot_5m.csv")
    assert len(df)>0
