from __future__ import annotations

from astraquant.pricing.intrinsic import OptionPricing
from astraquant.pricing.strike_selector import StrikeSelector
from astraquant.scanners.candle_matcher import CandleMatcher
from astraquant.calendar.expiry_cycle import ExpiryCycle
from astraquant.config.index_config import INDEX_CONFIG


class DiscountScanner:

    def __init__(self, broker):

        self.broker = broker

    def scan(
        self,
        symbol: str = "NIFTY",
        option_type: str = "CE",
        interval: str = "5minute",
        threshold: float = 5.0,
    ):
        config = INDEX_CONFIG[symbol]
        cycle = ExpiryCycle.current(
            expiry_weekday=config["expiry_weekday"],
        )
        
        print("=" * 100)
        print("DIDRS DISCOUNT SCANNER")
        print("=" * 100)
        print(f"Index          : {symbol}")
        print(f"Option Type    : {option_type}")
        print(f"Time Frame     : {interval}")
        print("=" * 100)
        start = cycle.scan_start
        end = cycle.scan_end
        if cycle.is_expiry_day and not cycle.allow_new_trade:

            print()
            print("=" * 100)
            print("DIDRS ENTRY BLOCKED")
            print("Reason : Expiry day after 11:00 AM")
            print("=" * 100)
            print()

            return
        print("=" * 100)
        print("Downloading Spot History...")
        print(f"Previous Expiry : {cycle.previous_expiry.date()}")
        print(f"Next Expiry     : {cycle.next_expiry.date()}")
        print(f"Scan Start      : {start}")
        print(f"Scan End        : {end}")
        print(f"Trade Allowed   : {cycle.allow_new_trade}")
        print("=" * 100)




        spot = self.broker.history.get_historical_candles(
            instrument_key=config["spot_key"],
            interval=interval,
            to_date=end.strftime("%Y-%m-%d"),
            start_datetime=start,
            end_datetime=end,
        )

        if not spot:
            print("No spot candles found.")
            return

        latest_spot = spot[-1].close
        print(f"Latest Candle Time : {spot[-1].timestamp}")
        print(f"Latest Spot        : {latest_spot}")

        strike = StrikeSelector.deep_itm_call(
            spot=latest_spot,
            offset=config["anchor_interval"],
        )

        print(f"Latest Spot : {latest_spot:.2f}")
        print(f"Selected Strike : {strike}")
        print(f"Anchor Interval : {config['anchor_interval']}")

        instrument = self.broker.instruments.find_option(
            symbol=config["option_prefix"],
            strike=strike,
            option_type=option_type,
        )

        print(f"Option : {instrument['trading_symbol']}")

        print("Downloading Option History...")

        option = self.broker.history.get_historical_candles(
            instrument_key=instrument["instrument_key"],
            interval=interval,
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
        print("\nFirst 5 Spot candles")
        for c in spot[:5]:
            print(c.timestamp)

        print("\nFirst 5 Option candles")
        for c in option[:5]:
            print(c.timestamp)
            
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
#            print(
#                f"{spot_candle.timestamp.strftime('%H:%M')}  "
#                f"Spot={spot_candle.close:.2f}  "
#                f"Option={option_candle.close:.2f}  "
#                f"Intrinsic={intrinsic:.2f}  "
#                f"Discount={discount:.2f}"
#            )

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