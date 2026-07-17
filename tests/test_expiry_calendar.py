from datetime import date

from astraquant.calendar.expiry_calendar import ExpiryCalendar

today = date.today()

print("Today            :", today)
print("Previous Expiry  :", ExpiryCalendar.previous_expiry(today))
print("Next Expiry      :", ExpiryCalendar.next_expiry(today))
print("Is Expiry Day    :", ExpiryCalendar.is_expiry_day(today))