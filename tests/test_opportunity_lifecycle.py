from datetime import datetime
import time

from astraquant.alerts.alert import Alert
from astraquant.alerts.alert_engine import AlertEngine
from astraquant.scanners.models.discount_event import DiscountEvent
from astraquant.signals.didrs_signal import DidrsSignal
from astraquant.tracker.opportunity_status import OpportunityStatus
from astraquant.tracker import (
    DiscountSnapshot,
    DiscountTracker,
    OpportunityManager,
)

tracker = DiscountTracker()
manager = OpportunityManager()

discounts = [
    6.0,    # NEW
    9.5,    # IMPROVING
    9.7,    # STABLE
    7.0,    # WEAKENING
    1.0,    # RECOVERED
    12.5,   # IMPROVING
    1.0,    # RECOVERED
]

print("=" * 80)
print("ASTRAQUANT OPPORTUNITY LIFECYCLE TEST")
print("=" * 80)
for discount in discounts:

    snapshot = DiscountSnapshot(
        symbol="NIFTY",
        timestamp=datetime.now(),

        spot=25000,
        option_price=500,
        intrinsic=510,

        discount=discount,

        option_symbol="NIFTY25000CE",
    )

    tracker_result = tracker.update(snapshot)

    lifecycle = manager.update(tracker_result)

    if lifecycle.status == OpportunityStatus.CLOSED:
        tracker.reset(snapshot.symbol)

    signal = DidrsSignal.generate(
        current_discount=discount,
        threshold=5.0,
    )

    event = DiscountEvent(
        timestamp=datetime.now(),
        spot=25000,
        option=500,
        intrinsic=510,
        discount=discount,
    )

    alert = Alert(
        symbol="NIFTY",
        option="NIFTY25000CE",
        signal=signal.action,
        current_discount=discount,
        top_discount=[event],
        opportunity=lifecycle,
    )

    print()
    print("-" * 80)
    print(f"Discount : {discount:.2f}")
    print(f"Signal   : {signal.action}")
    print(f"State    : {lifecycle.state.value}")
    print(f"Status   : {lifecycle.status.value}")
    print(f"Max      : {lifecycle.max_discount:.2f}")

    AlertEngine.notify(alert)

    time.sleep(3)

print()
print("=" * 80)
print("TEST COMPLETED")
print("=" * 80)