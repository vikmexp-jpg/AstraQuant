from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime

from astraquant.logger import logger



class InstrumentRepository:

    def __init__(self, json_file: Path):

        with open(json_file, "r", encoding="utf-8") as fp:
            self.data = json.load(fp)

        logger.info(f"Loaded {len(self.data):,} instruments.")


    def find_option(
        self,
        symbol: str,
        strike: int,
        option_type: str,
        trading_date: str | None = None,
    ):

        if trading_date is None:
            trading_date = datetime.now().date()
        else:
            trading_date = datetime.strptime(
                trading_date,
                "%Y-%m-%d",
            ).date()

        candidates = []

        for item in self.data:

            if (
                item.get("underlying_symbol") == symbol
                and int(float(item.get("strike_price", 0))) == strike
                and item.get("instrument_type") == option_type
            ):

                expiry = datetime.fromtimestamp(
                    item["expiry"] / 1000
                ).date()

                if expiry >= trading_date:

                    candidates.append(
                        (
                            expiry,
                            item,
                        )
                    )

        if not candidates:
            return None

        candidates.sort(
            key=lambda x: x[0]
        )

        return candidates[0][1]