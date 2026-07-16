from astraquant.broker.upstox.order_service import (
    UpstoxOrderService,
)


def test_create_service():

    service = UpstoxOrderService(None)

    assert service is not None