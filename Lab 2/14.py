from collections import Counter
def solve():
    try:
        n = int(input())
        arr = list(map(int, input().split()))
    except EOFError:
        return
    cnt = Counter(arr)
    max_freq = max(cnt.values())
    cand = [item for item, freq in cnt.items() if freq == max_freq]
    print(min(cand))
solve()