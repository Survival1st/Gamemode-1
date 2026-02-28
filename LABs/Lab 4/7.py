import sys

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

def main():
    try:
        input_str = sys.stdin.read().strip()
        if not input_str:
            return

        rev_iterator = Reverse(input_str)
        
        for char in rev_iterator:
            sys.stdout.write(char)
        sys.stdout.write('\n')
            
    except EOFError:
        pass

if __name__ == "__main__":
    main()