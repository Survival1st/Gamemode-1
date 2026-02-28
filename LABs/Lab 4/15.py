import math
from datetime import datetime, timedelta, timezone

def solve():
    def parse_dt(s):
        parts = s.split(' UTC')
        dt_str = parts[0]
        tz_str = parts[1]
        
        sign = 1 if tz_str[0] == '+' else -1
        h, m = map(int, tz_str[1:].split(':'))
        offset = timezone(timedelta(hours=sign * h, minutes=sign * m))
        
        dt = datetime.strptime(dt_str, "%Y-%m-%d")
        return dt.replace(tzinfo=offset)

    try:
        line1 = input().strip()
        line2 = input().strip()
        if not line1 or not line2:
            return
    except EOFError:
        return

    birth_dt = parse_dt(line1)
    curr_dt = parse_dt(line2)

    b_month, b_day = birth_dt.month, birth_dt.day

    target_years = [curr_dt.year, curr_dt.year + 1, curr_dt.year + 2]
    
    for year in target_years:
        ty_month, ty_day = b_month, b_day
        
        is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        if ty_month == 2 and ty_day == 29 and not is_leap:
            ty_month, ty_day = 2, 28
            
        bday_moment = datetime(year, ty_month, ty_day, tzinfo=birth_dt.tzinfo)
        
        delta = (bday_moment - curr_dt).total_seconds()
        
        if delta >= 0:
            if delta == 0:
                print(0)
            else:
                print(math.ceil(delta / 86400))
            return

if __name__ == "__main__":
    solve()