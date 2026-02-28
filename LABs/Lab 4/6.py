import sys

def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield str(a)
        a, b = b, a + b

def main():
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        
        n = int(input_data)
        if n <= 0:
            return

        gen = fibonacci_generator(n)
        
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