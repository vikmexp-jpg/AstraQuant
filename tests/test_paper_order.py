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


def test_paper_order():

    instrument = Instrument(
        instrument_key="NSE_FO|57340",
        trading_symbol="NIFTY 24000 CE",
        exchange="NSE",
        symbol="NIFTY",
        expiry="2026-07-21",
        strike=24000,
        option_type="CE",
        lot_size=65,
    )

    order = BrokerOrder(
        instrument=instrument,
        quantity=65,
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        product=ProductType.INTRADAY,
    )

    service = UpstoxOrderService(
        api_client=None,
        mode=TradingMode.PAPER,
    )

    order_id = service.place(order)

    assert order_id == "PAPER-ORDER-001"