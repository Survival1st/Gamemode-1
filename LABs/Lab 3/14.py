import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        n = int(line1.strip())
        
        line2 = sys.stdin.readline()
        if not line2: return
        a = list(map(int, line2.split()))
        
        line3 = sys.stdin.readline()
        if not line3: return
        q = int(line3.strip())
    except ValueError:
        return
    for _ in range(q):
        command = sys.stdin.readline().split()
        op = command[0]
        
        if op == "add":
            x = int(command[1])
            func = lambda val, x=x: val + x
        elif op == "multiply":
            x = int(command[1])
            func = lambda val, x=x: val * x
        elif op == "power":
            x = int(command[1])
            func = lambda val, x=x: val ** x
        elif op == "abs":
            func = lambda val: abs(val)
        a = [func(item) for item in a]
    print(*(a))

solve()