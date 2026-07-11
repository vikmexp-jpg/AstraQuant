from astraquant.utils import LoggerFactory


def test_logger_creation():

    logger = LoggerFactory.get_logger()

    assert logger.name == "AstraQuant"