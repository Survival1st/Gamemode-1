import sys

def limited_cycle(elements, k):
    for _ in range(k):
        for item in elements:
            yield item

def main():
    try:
        input_data = sys.stdin.read().splitlines()
        if not input_data or len(input_data) < 2:
            return
        
        elements = input_data[0].split()
        k = int(input_data[1])
        
        gen = limited_cycle(elements, k)
        
        first = True
        for val in gen:
            if not first:
                sys.stdout.write(' ')
            sys.stdout.write(val)
            first = False
        sys.stdout.write('\n')
            
    except (EOFError, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()