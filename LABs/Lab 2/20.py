import sys

def simulate_mongodb():
    inp_dt = sys.stdin.read().splitlines()
    if not inp_dt:
        return
    
    n = int(inp_dt[0])
    dct = {}
    
    for i in range(1, n + 1):
        command = inp_dt[i].split()
        
        if not command:
            continue
            
        action = command[0]
        
        if action == "set":
            key = command[1]
            value = command[2]
            dct[key] = value
        elif action == "get":
            key = command[1]
            if key in dct:
                print(dct[key])
            else:
                print(f"KE: no key {key} found in the document")
if __name__ == "__main__":
    simulate_mongodb()