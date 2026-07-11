from astraquant.core.models import Position


def test_position_creation():

    position = Position(
        symbol="NIFTY",
        quantity=25,
        average_price=250.5,
    )

    assert position.quantity == 25

    assert position.average_price == 250.5