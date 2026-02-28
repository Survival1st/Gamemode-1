import sys
import math

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        r = float(line1.strip())
        
        line2 = sys.stdin.readline()
        if not line2: return
        x1, y1 = map(float, line2.split())
        
        line3 = sys.stdin.readline()
        if not line3: return
        x2, y2 = map(float, line3.split())
    except ValueError:
        return

    dx = x2 - x1
    dy = y2 - y1
    
    a = dx**2 + dy**2
    
    if a == 0:
        if x1**2 + y1**2 <= r**2 + 1e-11:
            print(f"{0.0:.10f}")
        else:
            print(f"{0.0:.10f}")
        return

    b = 2 * (x1 * dx + y1 * dy)
    c = x1**2 + y1**2 - r**2
    
    dist_sq = b**2 - 4 * a * c
    
    if dist_sq < 0:
        print(f"{0.0:.10f}")
        return
    
    sqrt_d = math.sqrt(dist_sq)
    t1 = (-b - sqrt_d) / (2 * a)
    t2 = (-b + sqrt_d) / (2 * a)
    
    t_start = max(0.0, min(t1, t2))
    t_end = min(1.0, max(t1, t2))
    
    if t_start > t_end:
        print(f"{0.0:.10f}")
    else:
        overlap_len = (t_end - t_start) * math.sqrt(a)
        print(f"{overlap_len:.10f}")

if __name__ == "__main__":
    solve()