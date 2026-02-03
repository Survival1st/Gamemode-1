def apply(criterion, n):
    for i in range(n):
        if criterion(i):
            return True
    return False

def is_odd(x):
    return x % 2 == 1

res = apply(is_odd, 100)
