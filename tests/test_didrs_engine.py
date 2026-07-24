from datetime import datetime
from unittest.mock import MagicMock

from astraquant.didrs.didrs_engine import DidrsEngine
from astraquant.tracker.opportunity import Opportunity
from astraquant.tracker.opportunity_state import OpportunityState
from astraquant.tracker.opportunity_status import OpportunityStatus


def _scan_result(discount: float):
    result = MagicMock()

    result.symbol = "NIFTY"
    result.option_symbol = "NIFTY24500CE"

    result.timestamp = datetime.now()

    result.spot = 24500
    result.option_price = 500
    result.intrinsic = 510

    result.discount = discount

    result.top_discounts = []

    return result


def test_negative_discount_without_active_opportunity_is_ignored():

    engine = DidrsEngine(MagicMock())

    engine.scanner.scan = MagicMock(
        return_value=_scan_result(-5.0)
    )

    lifecycle = engine.run(
        symbol="NIFTY",
        threshold=5.0,
    )

    assert lifecycle is None

    assert engine.manager.active_opportunity("NIFTY") is None


def test_negative_discount_closes_active_opportunity():

    engine = DidrsEngine(MagicMock())
    # First scan - creates NEW opportunity
    engine.scanner.scan = MagicMock(
        return_value=_scan_result(10.0)
    )

    engine.run(
        symbol="NIFTY",
        threshold=5.0,
    )

    # Second scan - recovery
    engine.scanner.scan = MagicMock(
        return_value=_scan_result(1.0)
    )

    lifecycle = engine.run(
        symbol="NIFTY",
        threshold=5.0,
    )

    assert lifecycle.state == OpportunityState.RECOVERED
    assert lifecycle.status == OpportunityStatus.CLOSED




def test_multiple_negative_discounts_are_ignored():

    engine = DidrsEngine(MagicMock())

    negative_discounts = [
        -10.0,
        -8.5,
        -3.2,
        -15.0,
        -1.0,
    ]

    for discount in negative_discounts:

        result = MagicMock()

        result.symbol = "NIFTY"
        result.option_symbol = "NIFTY24500CE"

        result.timestamp = None

        result.spot = 24500
        result.option_price = 760
        result.intrinsic = 750

        result.discount = discount

        result.top_discounts = []

        engine.scanner.scan = MagicMock(
            return_value=result
        )

        lifecycle = engine.run(
            symbol="NIFTY",
            threshold=5.0,
        )

        #
        # Should completely ignore negative discounts.
        #
        assert lifecycle is None

        #
        # No active opportunity should exist.
        #
        assert (
            engine.manager.active_opportunity("NIFTY")
            is None
        )

        #
        # Tracker should not remember the symbol.
        #
        assert (
            "NIFTY"
            not in engine.tracker._previous
        )