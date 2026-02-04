import sys

def solve():
    inp_dt = sys.stdin.read().splitlines()
    if not inp_dt:
        return
    
    n = int(inp_dt[0])
    drm_cnt = {}
    
    for i in range(1, n + 1):
        l = inp_dt[i].split()
        if not l:
            continue
        
        name = l[0]
        ep = int(l[1])
        
        if name in drm_cnt:
            drm_cnt[name] += ep
        else:
            drm_cnt[name] = ep
            
    sort_nm = sorted(drm_cnt.keys())
    
    for name in sort_nm:
        print(f"{name} {drm_cnt[name]}")

if __name__ == "__main__":
    solve()