import sys
import json

def get_diff(obj1, obj2, path="", diff_list=None):
    if diff_list is None:
        diff_list = []
    
    keys1 = set(obj1.keys()) if isinstance(obj1, dict) else set()
    keys2 = set(obj2.keys()) if isinstance(obj2, dict) else set()
    all_keys = sorted(keys1 | keys2)

    for key in all_keys:
        current_path = f"{path}.{key}" if path else key
        
        val1 = obj1.get(key, "<missing>") if isinstance(obj1, dict) else "<missing>"
        val2 = obj2.get(key, "<missing>") if isinstance(obj2, dict) else "<missing>"

        if val1 == val2:
            continue

        if isinstance(val1, dict) and isinstance(val2, dict):
            get_diff(val1, val2, current_path, diff_list)
        else:
            s1 = json.dumps(val1, separators=(',', ':')) if val1 != "<missing>" else "<missing>"
            s2 = json.dumps(val2, separators=(',', ':')) if val2 != "<missing>" else "<missing>"
            diff_list.append(f"{current_path} : {s1} -> {s2}")
            
    return diff_list

def main():
    try:
        input_data = sys.stdin.read().splitlines()
        if len(input_data) < 2:
            return

        obj1 = json.loads(input_data[0])
        obj2 = json.loads(input_data[1])

        differences = get_diff(obj1, obj2)

        if not differences:
            print("No differences")
        else:
            for line in sorted(differences):
                print(line)

    except (EOFError, ValueError, json.JSONDecodeError):
        pass

if __name__ == "__main__":
    main()