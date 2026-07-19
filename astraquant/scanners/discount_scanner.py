from __future__ import annotations

from astraquant.pricing.intrinsic import OptionPricing
from astraquant.pricing.strike_selector import StrikeSelector
from astraquant.scanners.candle_matcher import CandleMatcher
from astraquant.calendar.expiry_cycle import ExpiryCycle
from astraquant.config.index_config import INDEX_CONFIG
from astraquant.scanners.models.scan_result import ScanResult
from astraquant.scanners.models.discount_event import DiscountEvent
from astraquant.logger import logger


class DiscountScanner:

    def __init__(self, broker):

        self.broker = broker

    def scan(
        self,
        symbol: str = "NIFTY",
        option_type: str = "CE",
        interval: str = "5 minute",
        threshold: float = 5.0,
    ):
        config = INDEX_CONFIG[symbol]
        cycle = ExpiryCycle.current(
            expiry_weekday=config["expiry_weekday"],
        )
        print("-" * 100)
        print()
        print("DIDRS DISCOUNT SCANNER")
        print(f"Index             : {symbol}")
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
        logger.debug("Downloading spot History...")
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

        strike = StrikeSelector.deep_itm_call(
            spot=latest_spot,
            offset=config["anchor_interval"],
        )

        instrument = self.broker.instruments.find_option(
            symbol=config["option_prefix"],
            strike=strike,
            option_type=option_type,
        )

        print(f"Option            : {instrument['trading_symbol']}")

        option = self.broker.history.get_historical_candles(
            instrument_key=instrument["instrument_key"],
            interval=interval,
            to_date=end.strftime("%Y-%m-%d"),
            start_datetime=start,
            end_datetime=end,
        )
        print(f"Scan Window       : {start.strftime('%Y-%m-%d %H:%M')} -> {end.strftime('%Y-%m-%d %H:%M')}")
        matched = CandleMatcher.match(
            spot,
            option,
        )

        count = 0
        current_discount = 0.0
        top_discounts = []

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
            
            current_discount = discount

            if discount >= threshold:

                count += 1

                top_discounts.append(
                    DiscountEvent(
                        timestamp=spot_candle.timestamp,
                        spot=spot_candle.close,
                        option=option_candle.close,
                        intrinsic=intrinsic,
                        discount=discount,
                    )
                )
                
        top_discounts.sort(
            key=lambda x: x.discount,
            reverse=True,
        )

        top_discounts = top_discounts[:2]
        print(f"Current Spot      : {latest_spot:.2f}")
        print(f"Current Discount  : {current_discount:.2f}")

        if top_discounts:

            print()
            print(
                f"{'Time':<8}"
                f"{'Spot':>20}"
                f"{'Option':>16}"
                f"{'Intrinsic':>17}"
                f"{'Discount':>14}"
            )
            print("-" * 80)

            for rank, item in enumerate(top_discounts, start=1):

                print(
                    f"{item.timestamp.strftime('%Y-%m-%d %H:%M'):<20}"
                    f"{item.spot:>12.2f}"
                    f"{item.option:>12.2f}"
                    f"{item.intrinsic:>14.2f}"
                    f"{item.discount:>14.2f}"
                )

        return ScanResult(
            symbol=symbol,
            option_symbol=instrument["trading_symbol"],
            strike=strike,
            current_spot=latest_spot,
            current_discount=current_discount,
            occurrences=count,
            top_discounts=top_discounts,
        )