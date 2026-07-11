from astraquant.config import ConfigLoader


def test_load_configuration():
    config = ConfigLoader.load()

    assert config["application"]["name"] == "AstraQuant"
    assert config["environment"]["mode"] == "backtest"