from __future__ import annotations

from astraquant.config.settings import (
    NIFTY_DISCOUNT_THRESHOLD,
    SENSEX_DISCOUNT_THRESHOLD,
)

INDEX_CONFIG = {

    "NIFTY": {
        "scan_enabled": True,
        "spot_key": "NSE_INDEX|Nifty 50",
        "anchor_interval": 500,
        "expiry_weekday": 1,
        "option_prefix": "NIFTY",
        "discount_threshold": 2.0,
    },

    "SENSEX": {
        "scan_enabled": True,
        "spot_key": "BSE_INDEX|SENSEX",
        "anchor_interval": 1000,
        "expiry_weekday": 3,   # ✅ Thursday (Monday=0, Tuesday=1, Wednesday=2, Thursday=3)
        "option_prefix": "SENSEX",
        "discount_threshold": 30.0,
    },

    "BANKNIFTY": {
        "scan_enabled": False,
        "spot_key": "NSE_INDEX|Nifty Bank",
        "anchor_interval": 1000,
        "expiry_weekday": 2,
        "option_prefix": "BANKNIFTY",
        "discount_threshold": 20.0,
    },
}

if NIFTY_DISCOUNT_THRESHOLD is not None:
    INDEX_CONFIG["NIFTY"]["discount_threshold"] = NIFTY_DISCOUNT_THRESHOLD

if SENSEX_DISCOUNT_THRESHOLD is not None:
    INDEX_CONFIG["SENSEX"]["discount_threshold"] = SENSEX_DISCOUNT_THRESHOLD
