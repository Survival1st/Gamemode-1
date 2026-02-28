import sys

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

def main():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        a = int(input_data[0])
        b = int(input_data[1])
        
        for val in squares(a, b):
            sys.stdout.write(str(val) + '\n')
            
    except (EOFError, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()