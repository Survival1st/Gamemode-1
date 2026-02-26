# Example 1
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current date:", current_date)
print("5 days earlier:", new_date)

# Example 2
from datetime import datetime, timedelta
today = datetime.today()
yesterday = today - timedelta(days=1, hours = 5)
tomorrow = today + timedelta(days=1)
print("Today: ", today)
print("Tomorrow: ", tomorrow)
print("Yesterday: ", yesterday)

# Example 3
from datetime import datetime

now = datetime.now()
print("Original:", now)
no_microseconds = now.replace(microsecond=0)
print("Without microseconds:", no_microseconds)

# Example 4
from datetime import datetime

t1 = datetime.fromisoformat("2026-02-26 12:00:00")
t2 = datetime.fromisoformat("2026-02-26 13:38:27")

print(abs((t2 - t1).total_seconds()))