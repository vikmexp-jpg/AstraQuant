from astraquant.version import APPLICATION_NAME, VERSION


def test_application_name():
    assert APPLICATION_NAME == "AstraQuant"


def test_version():
    assert VERSION == "1.0.0-alpha"