n = int(input())
numbers = map(int, input().split())
def square(num):
    return num ** 2
print(sum(map(square, numbers)))
