from astraquant.broker import (
    BrokerOrder,
    BrokerPosition,
    MarketQuote,
)


def test_market_quote():

    quote = MarketQuote(
        instrument="NIFTY",
        ltp=25000,
    )

    assert quote.ltp == 25000


def test_order():

    order = BrokerOrder(
        instrument="NIFTY",
        quantity=1,
        price=250,
        side="BUY",
    )

    assert order.side == "BUY"


def test_position():

    position = BrokerPosition(
        instrument="NIFTY",
        quantity=2,
        average_price=200,
    )

    assert position.quantity == 2