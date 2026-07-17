from __future__ import annotations

from astraquant.pricing.intrinsic import OptionPricing
from astraquant.pricing.strike_selector import StrikeSelector
from astraquant.scanners.candle_matcher import CandleMatcher
from datetime import datetime


class DiscountScanner:

    def __init__(self, broker):

        self.broker = broker

    def scan(
        self,
        spot_key: str,
        symbol: str = "NIFTY",
        option_type: str = "CE",
        threshold: float = 5.0,
    ):

        print("=" * 100)
        print("Downloading Spot History...")



        start = datetime.fromisoformat(
            "2026-07-15T14:00:00+05:30"
        )

        end = datetime.now().astimezone()

        spot = self.broker.history.get_historical_candles(
            instrument_key=spot_key,
            to_date=end.strftime("%Y-%m-%d"),
            start_datetime=start,
            end_datetime=end,
        )

        if not spot:
            print("No spot candles found.")
            return

        latest_spot = spot[-1].close

        strike = StrikeSelector.deep_itm_call(
            spot=latest_spot,
            levels=2,
        )

        print(f"Latest Spot : {latest_spot:.2f}")
        print(f"Selected Strike : {strike}")

        instrument = self.broker.instruments.find_option(
            symbol=symbol,
            strike=strike,
            option_type=option_type,
        )

        print(f"Option : {instrument['trading_symbol']}")

        print("Downloading Option History...")

        option = self.broker.history.get_historical_candles(
            instrument_key=instrument["instrument_key"],
            to_date=end.strftime("%Y-%m-%d"),
            start_datetime=start,
            end_datetime=end,
        )

        print("=" * 100)
        print("Scan Window")
        print(f"Start : {start}")
        print(f"End   : {end}")
        print("=" * 100)

        print(f"Spot Candles   : {len(spot)}")
        print(f"Option Candles : {len(option)}")

        matched = CandleMatcher.match(
            spot,
            option,
        )

        print(f"Matched Candles : {len(matched)}")

        print("\nFirst 10 matched candles:\n")

        for spot_candle, option_candle in matched[:10]:
            print(
                spot_candle.timestamp,
                " | ",
                option_candle.timestamp,
            )

        print("=" * 100)
        print(
            f"{'Time':<8}"
            f"{'Spot':>12}"
            f"{'Option':>12}"
            f"{'Intrinsic':>14}"
            f"{'Discount':>14}"
        )
        print("=" * 100)

        count = 0
        max_discount = float("-inf")
        best_spot = None
        best_option = None
        best_time = None
        best_intrinsic = None

        for spot_candle, option_candle in matched:

            intrinsic = OptionPricing.intrinsic_value(
                spot=spot_candle.close,
                strike=strike,
                option_type=option_type,
            )

            discount = OptionPricing.discount(
                spot=spot_candle.close,
                strike=strike,
                option_price=option_candle.close,
                option_type=option_type,
            )

            if discount >= threshold:

                count += 1

                if discount > max_discount:
                    max_discount = discount
                    best_time = spot_candle.timestamp
                    best_spot = spot_candle.close
                    best_option = option_candle.close
                    best_intrinsic = intrinsic

                print(
                    f"{spot_candle.timestamp.strftime('%Y-%m-%d %H:%M'):<20}"
                    f"{spot_candle.close:>12.2f}"
                    f"{option_candle.close:>12.2f}"
                    f"{intrinsic:>14.2f}"
                    f"{discount:>14.2f}"
                )

        print("=" * 100)
        print(f"Occurrences      : {count}")

        if count:

            print(f"Maximum Discount : {max_discount:.2f}")

            print()
            print("BEST DISCOUNT")
            print("-" * 40)
            print(f"Time       : {best_time}")
            print(f"Spot       : {best_spot:.2f}")
            print(f"Option     : {best_option:.2f}")
            print(f"Intrinsic  : {best_intrinsic:.2f}")
            print(f"Discount   : {max_discount:.2f}")

        print("=" * 100)