import sys

def solve():
    line1 = sys.stdin.readline()
    if not line1: return
    x1, y1 = map(float, line1.split())
    
    line2 = sys.stdin.readline()
    if not line2: return
    x2, y2 = map(float, line2.split())

    
    xp = x1 + (y1 * (x2 - x1)) / (y1 + y2)
    
    print(f"{xp:.10f} {0.0:.10f}")

if __name__ == "__main__":
    solve()