import sys

def countdown_generator(n):
    for i in range(n, -1, -1):
        yield str(i)

def main():
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        
        n = int(input_data)
        for val in countdown_generator(n):
            sys.stdout.write(val + '\n')
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()