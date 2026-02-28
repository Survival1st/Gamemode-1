import sys
from datetime import datetime, timezone, timedelta

def get_utc_timestamp(line):
    parts = line.split()
    date_str = parts[0]
    time_str = parts[1]
    tz_str = parts[2][3:]
    
    y, m, d = map(int, date_str.split('-'))
    hh, mm, ss = map(int, time_str.split(':'))
    
    sign = 1 if tz_str[0] == '+' else -1
    tz_h, tz_m = map(int, tz_str[1:].split(':'))
    
    offset = timedelta(hours=tz_h, minutes=tz_m)
    if sign == -1:
        offset = -offset
        
    dt = datetime(y, m, d, hh, mm, ss, tzinfo=timezone(offset))
    return int(dt.timestamp())

def solve():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return
        
    start_ts = get_utc_timestamp(lines[0])
    end_ts = get_utc_timestamp(lines[1])
    
    print(end_ts - start_ts)

if __name__ == "__main__":
    solve()