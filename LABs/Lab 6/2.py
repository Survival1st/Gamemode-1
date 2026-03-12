n = int(input())
nums = list(map(int, input().split()))
def is_even(x):
    return x % 2 == 0
even_numbers = filter(is_even, nums)

print(sum(even_numbers))
        