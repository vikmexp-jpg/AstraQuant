from astraquant.broker import (
    BrokerOrder,
    Instrument,
    OrderSide,
    OrderStatus,
    OrderType,
    ProductType,
)


def test_order_model():

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

    assert order.side == OrderSide.BUY
    assert order.status == OrderStatus.PENDING
    assert order.instrument.symbol == "NIFTY"