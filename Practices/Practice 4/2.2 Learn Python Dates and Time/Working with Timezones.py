# Exaample 1
from datetime import datetime
from zoneinfo import ZoneInfo

dt_utc = datetime.now(ZoneInfo("UTC"))
dt_tokyo = datetime.now(ZoneInfo("Asia/Tokyo"))

print(dt_utc)
print(dt_tokyo)

# Example 2
from datetime import datetime
from zoneinfo import ZoneInfo

nyc_zone = ZoneInfo("America/New_York")
london_zone = ZoneInfo("Europe/London")

nyc_time = datetime(2026, 2, 24, 10, 0, tzinfo=nyc_zone)
london_time = nyc_time.astimezone(london_zone)

print(f"New York: {nyc_time}")
print(f"London: {london_time}")

# Example 3
from datetime import datetime
from zoneinfo import ZoneInfo

def check_dst(dt_obj, zone_name):
    zone = ZoneInfo(zone_name)
    dt_aware = dt_obj.replace(tzinfo=zone)
    
    is_dst = dt_aware.dst() != None and dt_aware.dst().total_seconds() != 0
    return f"{zone_name} DST active: {is_dst}"

summer = datetime(2026, 7, 1)
winter = datetime(2026, 1, 1)

print(check_dst(summer, "America/Los_Angeles"))
print(check_dst(winter, "America/Los_Angeles"))

utc_now = datetime.now(ZoneInfo("UTC"))
local_now = utc_now.astimezone()
print(f"Local System Timezone: {local_now.tzname()}")