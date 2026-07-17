import pytest

from astraquant.broker import (
    BrokerOrder,
    Instrument,
    OrderSide,
    OrderType,
    ProductType,
    TradingMode,
)
from astraquant.broker.upstox.order_service import (
    UpstoxOrderService,
)


def test_invalid_quantity():

    instrument = Instrument(
        instrument_key="NSE_FO|1",
        trading_symbol="TEST",
        exchange="NSE",
        symbol="NIFTY",
        expiry="2026-07-21",
        strike=24000,
        option_type="CE",
        lot_size=65,
    )

    order = BrokerOrder(
        instrument=instrument,
        quantity=0,
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        product=ProductType.INTRADAY,
    )

    service = UpstoxOrderService(
        api_client=None,
        mode=TradingMode.PAPER,
    )

    with pytest.raises(ValueError):
        service.place(order)