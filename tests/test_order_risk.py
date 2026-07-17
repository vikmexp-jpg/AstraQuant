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


def instrument():

    return Instrument(
        instrument_key="NSE_FO|1",
        trading_symbol="TEST",
        exchange="NSE",
        symbol="NIFTY",
        expiry="2026-07-21",
        strike=24000,
        option_type="CE",
        lot_size=65,
    )


def test_invalid_lot_size():

    order = BrokerOrder(
        instrument=instrument(),
        quantity=10,
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


def test_limit_order_without_price():

    order = BrokerOrder(
        instrument=instrument(),
        quantity=65,
        side=OrderSide.BUY,
        order_type=OrderType.LIMIT,
        product=ProductType.INTRADAY,
    )

    service = UpstoxOrderService(
        api_client=None,
        mode=TradingMode.PAPER,
    )

    with pytest.raises(ValueError):
        service.place(order)