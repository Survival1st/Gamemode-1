def isUsual(n):
    if n <= 0:
        return False
    
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
            
    return n == 1

num = int(input())

if isUsual(num):
    print("Yes")
else:
    print("No")
