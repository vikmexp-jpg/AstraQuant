from pathlib import Path
from datetime import datetime

from astraquant.instruments.repository import InstrumentRepository

root = Path(__file__).resolve().parents[1]

repo = InstrumentRepository(
    root
    / "astraquant"
    / "data"
    / "instruments"
    / "upstox.json"
)

count = 0

for item in repo.data:

    if (
        item.get("underlying_symbol") == "NIFTY"
        and item.get("strike_price") == 23600.0
        and item.get("instrument_type") == "CE"
    ):

        expiry = datetime.fromtimestamp(
            item["expiry"] / 1000
        )

        print(
            expiry.date(),
            item["trading_symbol"],
        )

        count += 1

print()

print("Total:", count)