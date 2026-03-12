n = int(input())
numbers = map(int, input().split())
unique_sorted_numbers = sorted(set(numbers))
print(*(unique_sorted_numbers))