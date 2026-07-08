import logging

from astraquant.constants import LOG_FORMAT


def get_logger(name: str):

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    console = logging.StreamHandler()

    formatter = logging.Formatter(LOG_FORMAT)

    console.setFormatter(formatter)

    logger.addHandler(console)

    return logger