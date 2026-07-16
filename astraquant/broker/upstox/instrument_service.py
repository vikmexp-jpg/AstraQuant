from __future__ import annotations

from astraquant.broker import Instrument
from astraquant.broker.instrument import InstrumentService
import os

import requests


class UpstoxInstrumentService(InstrumentService):
    """
    Upstox implementation of InstrumentService.
    """

    def __init__(self, api_client):

        self.api_client = api_client

    def find_option(
        self,
        symbol: str,
        strike: int,
        option_type: str,
    ) -> Instrument:

        token = os.getenv("UPSTOX_ACCESS_TOKEN")

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
        }

        params = {
            "query": f"{symbol} {strike}",
            "segments": "FO",
            "instrument_types": option_type,
            "page_number": 1,
            "records": 10,
        }

        response = requests.get(
            "https://api.upstox.com/v2/instruments/search",
            headers=headers,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        payload = response.json()
        data = payload.get("data", [])

        if not data:
            raise LookupError("Instrument not found.")

        item = data[0]

        return Instrument(
            instrument_key=item["instrument_key"],
            trading_symbol=item["trading_symbol"],
            exchange=item["exchange"],
            symbol=item["underlying_symbol"],
            expiry=item["expiry"],
            strike=int(item["strike_price"]),
            option_type=item["instrument_type"],
            lot_size=int(item["lot_size"]),
        )

    def find_future(
        self,
        symbol: str,
        expiry: str,
    ) -> Instrument:

        raise NotImplementedError