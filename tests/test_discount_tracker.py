from datetime import datetime

from astraquant.tracker import (
    DiscountSnapshot,
    DiscountTracker,
    OpportunityState,
)


def test_first_discount_creates_new_opportunity():

    tracker = DiscountTracker()

    snapshot = DiscountSnapshot(
        symbol="NIFTY",
        timestamp=datetime.now(),
        spot=25000,
        option_price=510,
        intrinsic=520,
        discount=10,
        option_symbol="NIFTY25000CE",
    )

    result = tracker.update(snapshot)

    assert result.state == OpportunityState.NEW

def test_same_discount_is_stable():

    tracker = DiscountTracker()

    snapshot1 = DiscountSnapshot(
        symbol="NIFTY",
        timestamp=datetime.now(),
        spot=25000,
        option_price=510,
        intrinsic=520,
        discount=10,
        option_symbol="NIFTY25000CE",
    )

    tracker.update(snapshot1)

    snapshot2 = DiscountSnapshot(
        symbol="NIFTY",
        timestamp=datetime.now(),
        spot=25000,
        option_price=510,
        intrinsic=520,
        discount=10,
        option_symbol="NIFTY25000CE",
    )

    result = tracker.update(snapshot2)

    assert result.state == OpportunityState.STABLE

def test_discount_increase_creates_improving():

    tracker = DiscountTracker()

    tracker.update(
        DiscountSnapshot(
            symbol="NIFTY",
            timestamp=datetime.now(),
            spot=25000,
            option_price=510,
            intrinsic=520,
            discount=10,
            option_symbol="NIFTY25000CE",
        )
    )

    result = tracker.update(
        DiscountSnapshot(
            symbol="NIFTY",
            timestamp=datetime.now(),
            spot=25000,
            option_price=510,
            intrinsic=520,
            discount=13,
            option_symbol="NIFTY25000CE",
        )
    )

    assert result.state == OpportunityState.IMPROVING

def test_discount_drop_creates_weakening():

    tracker = DiscountTracker()

    tracker.update(
        DiscountSnapshot(
            symbol="NIFTY",
            timestamp=datetime.now(),
            spot=25000,
            option_price=510,
            intrinsic=520,
            discount=12,
            option_symbol="NIFTY25000CE",
        )
    )

    result = tracker.update(
        DiscountSnapshot(
            symbol="NIFTY",
            timestamp=datetime.now(),
            spot=25000,
            option_price=510,
            intrinsic=520,
            discount=8,
            option_symbol="NIFTY25000CE",
        )
    )

    assert result.state == OpportunityState.WEAKENING

def test_discount_below_recovery_threshold():

    tracker = DiscountTracker()

    tracker.update(
        DiscountSnapshot(
            symbol="NIFTY",
            timestamp=datetime.now(),
            spot=25000,
            option_price=510,
            intrinsic=520,
            discount=12,
            option_symbol="NIFTY25000CE",
        )
    )

    result = tracker.update(
        DiscountSnapshot(
            symbol="NIFTY",
            timestamp=datetime.now(),
            spot=25000,
            option_price=510,
            intrinsic=520,
            discount=1,
            option_symbol="NIFTY25000CE",
        )
    )

    assert result.state == OpportunityState.RECOVERED