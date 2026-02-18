n = int(input())

squares_gen = (x**2 for x in range(1, n + 1))

for i in range(1, n + 1):
    print(next(squares_gen)) 


def C(x):
    for i in range(1, x + 1):
        yield i**2

n = int(input())
squares_gen = C(n)
for i in range(1, n + 1):
    print(next(squares_gen))