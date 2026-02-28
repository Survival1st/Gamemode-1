import sys
import importlib

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    try:
        n = int(input_data[0])
    except ValueError:
        return

    for i in range(1, n + 1):
        try:
            line = input_data[i].split()
            if len(line) < 2:
                continue
            
            module_path, attr_name = line[0], line[1]
            
            try:
                mod = importlib.import_module(module_path)
            except ImportError:
                print("MODULE_NOT_FOUND")
                continue
            
            if not hasattr(mod, attr_name):
                print("ATTRIBUTE_NOT_FOUND")
            else:
                attr = getattr(mod, attr_name)
                if callable(attr):
                    print("CALLABLE")
                else:
                    print("VALUE")
                    
        except IndexError:
            break

if __name__ == "__main__":
    solve()