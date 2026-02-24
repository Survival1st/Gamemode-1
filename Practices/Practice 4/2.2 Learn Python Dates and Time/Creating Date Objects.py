# Example 1
from datetime import date

my_date = date(2026, 2, 24)

print(my_date)
print(my_date.year)
print(my_date.month)
print(my_date.day)

# Example 2
from datetime import date
import time

iso_date = date.fromisoformat("2026-12-31")
print(iso_date)

timestamp_date = date.fromtimestamp(time.time())
print(timestamp_date)

# Example 3
from datetime import date, datetime

dt_obj = datetime(2026, 5, 20, 15, 30)
extracted_date = dt_obj.date()

print(extracted_date)
print(extracted_date.weekday())
print(extracted_date.isocalendar())

new_date = extracted_date.replace(year=2027, month=1)
print(new_date)