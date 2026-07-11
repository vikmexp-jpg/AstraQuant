from __future__ import annotations

from pathlib import Path

from astraquant.core.models import trade

from .candle_synchronizer import CandleSynchronizer
from .trade_manager import TradeManager
from astraquant.strategies import DIDRSStrategy
from astraquant.data import CSVDataProvider


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

    def run(self) -> int:
        """
        Execute one complete historical backtest.

        Returns
        -------
        int
            Number of BUY signals generated.
        """

        spot = self.spot_provider.candles()
        option = self.option_provider.candles()

        candles = CandleSynchronizer.synchronize(
            spot,
            option,
        )

        self.signal_count = 0

        for index in range(len(candles) - 1):

            current = candles[index]
            next_candle = candles[index + 1]

            signal = self.strategy.evaluate(
                context=current,
                expected_premium=current.option.close + 25,
                strike=23500,
            )

            if signal is None:
                continue

            self.signal_count += 1

            self.trade_manager.register_signal(signal)

            trade = self.trade_manager.process_next_candle(
                current,
                next_candle,
            )

            if trade is not None:
                self.executed_trades.append(trade)

        return self.executed_trades

    @property
    def total_signals(self) -> int:
        return self.signal_count


    @property
    def total_trades(self) -> int:
        return len(self.executed_trades)