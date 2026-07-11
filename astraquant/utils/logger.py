from __future__ import annotations

import logging
from pathlib import Path


class LoggerFactory:
    """Creates the application logger."""

    _logger: logging.Logger | None = None

    @classmethod
    def get_logger(
        cls,
        level: str = "INFO",
        log_file: str = "logs/astraquant.log",
    ) -> logging.Logger:

        if cls._logger is not None:
            return cls._logger

        Path(log_file).parent.mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger("AstraQuant")

        logger.setLevel(getattr(logging, level.upper()))

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s"
        )

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        file_handler = logging.FileHandler(log_file)

        file_handler.setFormatter(formatter)

        logger.addHandler(console)
        logger.addHandler(file_handler)

        cls._logger = logger

        return logger