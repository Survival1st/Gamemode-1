def sqr(x):
    return int(x) * int(x)
a = list(input().split())
print(*list(map(sqr, a)))