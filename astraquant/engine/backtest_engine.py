from __future__ import annotations

from pathlib import Path

from astraquant import config
from astraquant.core.models import trade

from .candle_synchronizer import CandleSynchronizer
from .trade_manager import TradeManager
from astraquant.strategies import DIDRSStrategy
from astraquant.data import CSVDataProvider
from .premium_calculator import PremiumCalculator
from astraquant.utils import StrikeSelector
from astraquant.config.config_service import ConfigService


class BacktestEngine:
    """
    Historical backtesting engine.
    """

    def __init__(
        self,
        spot_csv: str | Path,
        option_csv: str | Path,
    ) -> None:

        self.spot_provider = CSVDataProvider(spot_csv)
        self.option_provider = CSVDataProvider(option_csv)

        self.strategy = DIDRSStrategy()

        self.trade_manager = TradeManager()
        self.executed_trades = []
        self.signal_count = 0

    def run(self) -> list:
        """
        Execute one complete historical backtest.
        """

        self.executed_trades = []
        self.signal_count = 0
        # Load configuration
        config = ConfigService.get()

        spot = self.spot_provider.candles()
        option = self.option_provider.candles()

        candles = CandleSynchronizer.synchronize(
            spot,
            option,
        )

        print("=" * 60)
        print(f"Spot Candles        : {len(spot)}")
        print(f"Option Candles      : {len(option)}")
        print(f"Synchronized        : {len(candles)}")
        print("=" * 60)

        for index in range(len(candles) - 1):

            current = candles[index]
            next_candle = candles[index + 1]

            #
            # STEP-1
            # Manage active trade
            #
            if self.trade_manager.current_trade is not None:

                self.trade_manager.manage_trade(current)

                self.trade_manager.check_stop_loss(current)

                self.trade_manager.check_end_of_day(current)

                #
                # Trade completed?
                #
                if (
                    self.trade_manager.current_trade.exit_price
                    is not None
                ):
                    self.executed_trades.append(
                        self.trade_manager.current_trade
                    )

                    self.trade_manager.reset_for_reentry()

                continue

            #
            # STEP-2
            # Look for a new signal
            #
            strike = StrikeSelector.strike(
            spot_price=current.spot.close,
                offset=config["trading"]["strike_offset"],
            )

            expected = PremiumCalculator.expected_premium(
                current.spot,
                strike,
            )

            signal = self.strategy.evaluate(
                context=current,
                expected_premium=expected,
                strike=strike,
            )

            if signal is None:
                continue

            self.signal_count += 1

            self.trade_manager.register_signal(signal)

            self.trade_manager.process_next_candle(
                current,
                next_candle,
            )

        #
        # Safety:
        # If the backtest ends with an open trade,
        # close it on the last available candle.
        #
        if self.trade_manager.current_trade is not None:

            last = candles[-1]

            self.trade_manager.current_trade.close(
                exit_time=last.option.timestamp,
                exit_price=last.option.close,
            )

            self.executed_trades.append(
                self.trade_manager.current_trade
            )

            self.trade_manager.reset_for_reentry()

        return self.executed_trades

    @property
    def total_signals(self) -> int:
        return self.signal_count


    @property
    def total_trades(self) -> int:
        return len(self.executed_trades)