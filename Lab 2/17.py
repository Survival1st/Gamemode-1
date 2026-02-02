import sys
def solve():
    l1 = sys.stdin.readline()
    if not l1:
        return
    n = int(l1.strip())
    cnt = {}
    for _ in range(n):
        num = sys.stdin.readline().strip()
        if num:
            cnt[num] = cnt.get(num, 0) + 1
    ex_three = 0
    for phone in cnt:
        if cnt[phone] == 3:
            ex_three += 1
    print(ex_three)
if __name__ == "__main__":
    solve()