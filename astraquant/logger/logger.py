from __future__ import annotations

import logging
from pathlib import Path
from datetime import datetime

LOG_DIR = Path(__file__).resolve().parents[2] / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / f"{datetime.now():%Y-%m-%d}.log"

logger = logging.getLogger("AstraQuant")
logger.setLevel(logging.INFO)
logger.propagate = False

formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-7s | %(message)s",
    datefmt="%H:%M:%S",
)

if not logger.handlers:
    file = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file.setLevel(logging.INFO)
    file.setFormatter(formatter)
    logger.addHandler(file)