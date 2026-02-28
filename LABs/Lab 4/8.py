import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield str(i)

def main():
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        
        n = int(input_data)
        gen = prime_generator(n)
        
        first = True
        for val in gen:
            if not first:
                sys.stdout.write(' ')
            sys.stdout.write(val)
            first = False
        sys.stdout.write('\n')
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()