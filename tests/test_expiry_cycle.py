from astraquant.calendar.expiry_cycle import ExpiryCycle

cycle = ExpiryCycle.current()

print()

print("Previous Expiry :", cycle.previous_expiry)
print("Next Expiry     :", cycle.next_expiry)

print()

print("Scan Start      :", cycle.scan_start)
print("Scan End        :", cycle.scan_end)

print()

print("Expiry Day      :", cycle.is_expiry_day)
print("Trade Allowed   :", cycle.allow_new_trade)