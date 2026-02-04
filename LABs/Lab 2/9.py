n = int(input())
m = list(map(int, input().split()))
maxl = max(m)
minl = min(m)
for i in range(n):
    if m[i] == maxl:
        m[i] = minl
print(*m)
        