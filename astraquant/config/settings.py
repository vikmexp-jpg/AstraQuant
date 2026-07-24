from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
from datetime import time

# Market timings
MARKET_OPEN = time(9, 15)
MARKET_CLOSE = time(15, 30)
#Work Around Broker was not providing correct data for Sensex before 9:25 AM, so started scan after 9:25 AM
DIDRS_SCAN_START = time(9, 15)
EXPIRY_ENTRY_CUTOFF = time(14, 0)

# DIDRS configuration
EXPIRY_SCAN_START = time(14, 0)

# Strike Selection
DEFAULT_LEVELS = 2        # 23500 CE when spot is 24081

# Discount
DEFAULT_DISCOUNT_THRESHOLD = 5.0

load_dotenv(ROOT_DIR / ".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")



def _parse_discount_threshold(value: str | None) -> float | None:
    if value is None or not value.strip():
        return None
    try:
        return float(value)
    except ValueError as exc:
        raise RuntimeError(
            f"Discount threshold must be a number, got: {value!r}"
        ) from exc

NIFTY_DISCOUNT_THRESHOLD = _parse_discount_threshold(
    os.getenv("DISCOUNT_THRESHOLD_NIFTY")
)
SENSEX_DISCOUNT_THRESHOLD = _parse_discount_threshold(
    os.getenv("DISCOUNT_THRESHOLD_SENSEX")
)

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is missing in .env")

if not TELEGRAM_CHAT_ID:
    raise RuntimeError("TELEGRAM_CHAT_ID is missing in .env")
