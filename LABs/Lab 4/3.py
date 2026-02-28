import sys

def divisibility_generator(n):
    for i in range(0, n + 1, 12):
        yield str(i)

def main():
    line = sys.stdin.read().strip()
    if not line:
        return
    
    limit = int(line)
    gen = divisibility_generator(limit)
    
    first = True
    for val in gen:
        if not first:
            sys.stdout.write(' ')
        sys.stdout.write(val)
        first = False
    sys.stdout.write('\n')

if __name__ == "__main__":
    main()