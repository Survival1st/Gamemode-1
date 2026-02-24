# Example 1
from datetime import datetime

now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)

# Example 2
from datetime import datetime

date_string = "2026-02-24 14:30:00"
date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

print(date_object)

formatted_date = date_object.strftime("%A, %B %d, %Y")
print(formatted_date)

# Example 3
from datetime import datetime, timedelta

start_date = datetime.now()
duration = timedelta(days=10, hours=5)

future_date = start_date + duration
past_date = start_date - duration

print(f"Future: {future_date}")
print(f"Past: {past_date}")

difference = future_date - start_date
print(f"Total seconds: {difference.total_seconds()}")

