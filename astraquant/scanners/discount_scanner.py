from __future__ import annotations

from astraquant.calendar.expiry_cycle import ExpiryCycle
from astraquant.config.index_config import INDEX_CONFIG
from astraquant.logger import logger
from astraquant.pricing.intrinsic import OptionPricing
from astraquant.pricing.strike_selector import StrikeSelector
from astraquant.scanners.candle_matcher import CandleMatcher
from astraquant.scanners.models.discount_event import DiscountEvent
from astraquant.scanners.models.scan_result import ScanResult


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

        logger.info("-" * 100)
        logger.info("DIDRS DISCOUNT SCANNER")
        logger.info("Index : %s", symbol)

        if cycle.is_expiry_day and not cycle.allow_new_trade:

            logger.warning(
                "DIDRS entry blocked. Expiry day after 11:00 AM."
            )
            return None

        #
        # Download Spot History
        #
        spot_candles = self.broker.history.get_historical_candles(
            instrument_key=config["spot_key"],
            interval=interval,
            to_date=cycle.scan_end.strftime("%Y-%m-%d"),
            start_datetime=cycle.scan_start,
            end_datetime=cycle.scan_end,
        )

        if not spot_candles:

            logger.warning("No Spot candles found.")
            return None

        current_spot = spot_candles[-1].close

        strike = StrikeSelector.deep_itm_call(
            spot=current_spot,
            offset=config["anchor_interval"],
        )

        instrument = self.broker.instruments.find_option(
            symbol=config["option_prefix"],
            strike=strike,
            option_type=option_type,
        )

        option_candles = self.broker.history.get_historical_candles(
            instrument_key=instrument["instrument_key"],
            interval=interval,
            to_date=cycle.scan_end.strftime("%Y-%m-%d"),
            start_datetime=cycle.scan_start,
            end_datetime=cycle.scan_end,
        )

        matched = CandleMatcher.match(
            spot_candles,
            option_candles,
        )

        occurrences = 0
        discount_events: list[DiscountEvent] = []

        current_timestamp = None
        current_option_price = 0.0
        current_intrinsic = 0.0
        current_discount = 0.0

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

            #
            # Latest candle
            #
            current_timestamp = spot_candle.timestamp
            current_spot = spot_candle.close
            current_option_price = option_candle.close
            current_intrinsic = intrinsic
            current_discount = discount

            #
            # Historical opportunity
            #
            if discount >= threshold:

                occurrences += 1

                discount_events.append(
                    DiscountEvent(
                        timestamp=spot_candle.timestamp,
                        spot=spot_candle.close,
                        option=option_candle.close,
                        intrinsic=intrinsic,
                        discount=discount,
                    )
                )
            else:

                logger.debug(
                    "[%s] %-11s %-8s Current=%6.2f Max=%6.2f",
                    symbol,
                    "DISCOUNT",
                    "SKIPPED",
                    discount,
                    0.0,
                )

        #
        # Historical analysis
        #
        top_discounts = sorted(
            discount_events,
            key=lambda event: event.discount,
            reverse=True,
        )[:2]

        logger.info(
            "[%s] Current | Time=%s Spot=%.2f Option=%.2f Intrinsic=%.2f Discount=%.2f",
            symbol,
            current_timestamp.strftime("%H:%M"),
            current_spot,
            current_option_price,
            current_intrinsic,
            current_discount,
        )

        return ScanResult(
            symbol=symbol,
            option_symbol=instrument["trading_symbol"],
            strike=strike,
            timestamp=current_timestamp,
            spot=current_spot,
            option_price=current_option_price,
            intrinsic=current_intrinsic,
            discount=current_discount,
            occurrences=occurrences,
            top_discounts=top_discounts,
        )