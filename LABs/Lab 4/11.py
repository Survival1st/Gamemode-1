import sys
import json

def apply_patch(source, patch):
    if not isinstance(patch, dict):
        return patch
    
    if not isinstance(source, dict):
        source = {}

    for key, value in patch.items():
        if value is None:
            if key in source:
                del source[key]
        else:
            if key in source and isinstance(source[key], dict) and isinstance(value, dict):
                source[key] = apply_patch(source[key], value)
            else:
                source[key] = apply_patch({}, value)
    
    return source

def main():
    try:
        lines = sys.stdin.read().splitlines()
        if len(lines) < 2:
            return

        source_obj = json.loads(lines[0])
        patch_obj = json.loads(lines[1])

        result = apply_patch(source_obj, patch_obj)

        print(json.dumps(result, sort_keys=True, separators=(',', ':')))

    except (EOFError, ValueError, json.JSONDecodeError):
        pass

if __name__ == "__main__":
    main()