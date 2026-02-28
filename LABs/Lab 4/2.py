# Attempt 1
"""def C(x):
    for i in range(0, x + 1):
        if i % 2 == 0:
            yield i

n = int(input())
two_gen = C(n)
b = ",".join(map(str, two_gen))
print(b)"""

# Attempt 2
'''def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i
try:
    n = int(input())
    gen = even_generator(n)
    print(",".join(map(str, gen)))
    
except ValueError:
    pass'''

# Attempt 3
'''def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)
try:
    n = int(input())
    result = ",".join(even_numbers_generator(n))
    print(result)
except EOFError:
    pass'''

# Attempt 4
import sys

def even_generator(n):
    for i in range(0, n + 1, 2):
        yield str(i)

def main():
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        
        n = int(input_data)
        gen = even_generator(n)
        
        first = True
        for val in gen:
            if not first:
                sys.stdout.write(',')
            sys.stdout.write(val)
            first = False
        sys.stdout.write('\n')
        
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()
