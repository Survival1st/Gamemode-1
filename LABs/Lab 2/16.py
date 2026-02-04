def check_newbies():
    try:
        n = int(input())
        arr = list(map(int, input().split()))
    except EOFError:
        return
    seen = set()
    rlt = []
    for num in arr:
        if num not in seen:
            rlt.append("YES")
            seen.add(num)
        else:
            rlt.append("NO")
    print("\n".join(rlt))
check_newbies()