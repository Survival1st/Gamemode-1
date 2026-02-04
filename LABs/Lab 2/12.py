n = int(input())
arr = list(map(int, input().split()))
sqr = [x**2 for x in arr]
print(*(sqr))