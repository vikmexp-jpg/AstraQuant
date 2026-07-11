from datetime import datetime

from astraquant.core.models import (
    Trade,
)
from astraquant.engine import (
    CandleSynchronizer,
    TradeManager,
)

from tests.test_trade_manager import candle


def test_end_of_day_exit():

    manager = TradeManager()

    manager.current_trade = Trade(
        symbol="NIFTY",
        entry_time=datetime.now(),
        entry_price=200,
        quantity=1,
    )

    manager._trailing_stop = 190

    sync = CandleSynchronizer.synchronize(
        [
            candle(
                datetime(
                    2026,
                    1,
                    1,
                    15,
                    20,
                ),
                100,
                95,
            )
        ],
        [
            candle(
                datetime(
                    2026,
                    1,
                    1,
                    15,
                    20,
                ),
                210,
                205,
            )
        ],
    )[0]

    assert manager.check_end_of_day(sync)