from astraquant.startup import Startup


def test_startup_validation():

    config = Startup.validate()

    assert "application" in config