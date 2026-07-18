from __future__ import annotations

INDEX_CONFIG = {

    "NIFTY": {
        "scan_enabled": True,
        "spot_key": "NSE_INDEX|Nifty 50",
        "anchor_interval": 500,
        "expiry_weekday": 1,
        "option_prefix": "NIFTY",
        "discount_threshold": 10.0,
    },

    "SENSEX": {
        "scan_enabled": True,
        "spot_key": "BSE_INDEX|SENSEX",
        "anchor_interval": 1000,
        "expiry_weekday": 3,   # ✅ Thursday (Monday=0, Tuesday=1, Wednesday=2, Thursday=3)
        "option_prefix": "SENSEX",
        "discount_threshold": -200.0,
    },

    "BANKNIFTY": {
        "scan_enabled": False,
        "spot_key": "NSE_INDEX|Nifty Bank",
        "anchor_interval": 1000,
        "expiry_weekday": 2,
        "option_prefix": "BANKNIFTY",
        "discount_threshold": 5.0,
    },
}