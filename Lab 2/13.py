import math

def is_prime(n):
    if n <= 1:
        return "No"
    if n == 2:
        return "Yes"
    if n % 2 == 0:
        return "No"
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return "No"
    return "Yes"
num = int(input())
print(is_prime(num))