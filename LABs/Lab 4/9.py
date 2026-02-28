import sys

def powers_of_two(n):
    current = 1
    for i in range(n + 1):
        yield str(current)
        current *= 2

def main():
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        
        n = int(input_data)
        gen = powers_of_two(n)
        
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