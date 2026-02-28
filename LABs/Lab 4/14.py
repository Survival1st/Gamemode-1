import sys
from datetime import datetime, timedelta, timezone

def parse_to_utc(dt_str):
    parts = dt_str.split(' ')
    date_part = parts[0]
    tz_part = parts[1].replace('UTC', '')
    
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    
    sign = 1 if tz_part[0] == '+' else -1
    hours = int(tz_part[1:3])
    minutes = int(tz_part[4:6])
    
    offset = timezone(timedelta(hours=sign * hours, minutes=sign * minutes))
    return dt.replace(tzinfo=offset)

def main():
    try:
        lines = sys.stdin.read().splitlines()
        if len(lines) < 2:
            return

        dt1 = parse_to_utc(lines[0].strip())
        dt2 = parse_to_utc(lines[1].strip())

        diff_seconds = abs((dt1 - dt2).total_seconds())
        print(int(diff_seconds // 86400))

    except (ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()