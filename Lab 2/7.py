n = int(input())
numbers = list(map(int, input().split()))
max_number = max(numbers)
for i in range(n):
    if numbers[i] == max_number:
        print(i + 1)
        break