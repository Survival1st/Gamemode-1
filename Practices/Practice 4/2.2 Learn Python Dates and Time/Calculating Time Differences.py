# Example 1
from datetime import date

d1 = date(2026, 12, 31)
d2 = date(2026, 1, 1)

diff = d1 - d2
print(diff.days)

# Example 2
from datetime import datetime

now = datetime.now()
appointment = datetime(2026, 2, 25, 10, 0, 0)

time_left = appointment - now

print(time_left)
print(time_left.total_seconds())

# Example 3
from datetime import datetime, timedelta

def get_time_remaining(target_dt):
    now = datetime.now()
    delta = target_dt - now
    
    if delta.total_seconds() <= 0:
        return "Time is up!"
        
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"{days}d {hours}h {minutes}m {seconds}s"

deadline = datetime.now() + timedelta(days=2, hours=5, minutes=30)
print(get_time_remaining(deadline))