def count_unique_surnames():
    try:
        n = int(input())
        sn = []
        for _ in range(n):
            sn.append(input().strip())
    except EOFError:
        return
    uq_sn = set(sn)
    print(len(uq_sn))
count_unique_surnames()