n = int(input())
numbers = map(int, input().split())
result = sum(map(bool, numbers))
print(result)