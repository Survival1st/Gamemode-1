n = int(input())
m = list(map(int, input().split()))
sor = sorted(m, reverse=True)
print(*sor)  
        