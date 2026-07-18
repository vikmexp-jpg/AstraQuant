from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]

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
