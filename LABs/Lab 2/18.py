import sys

def solve():
    inp_dt = sys.stdin.read().split()
    if not inp_dt:
        return
    
    n = int(inp_dt[0])
    str = inp_dt[1:n+1]
    
    fst_occur = {}
    
    for i, s in enumerate(str, start=1):
        if s not in fst_occur:
            fst_occur[s] = i
            
    sort_key = sorted(fst_occur.keys())
    
    for key in sort_key:
        print(f"{key} {fst_occur[key]}")

if __name__ == "__main__":
    solve()