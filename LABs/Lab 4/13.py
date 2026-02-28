import sys
import json
import re

def resolve_query(data, query):
    tokens = re.findall(r'[^.\[\]]+|\[\d+\]', query)
    current = data
    
    try:
        for token in tokens:
            if token.startswith('['):
                index = int(token[1:-1])
                if not isinstance(current, list) or index >= len(current):
                    return "NOT_FOUND"
                current = current[index]
            else:
                if not isinstance(current, dict) or token not in current:
                    return "NOT_FOUND"
                current = current[token]
        
        return json.dumps(current, separators=(',', ':'))
    except (IndexError, TypeError, KeyError, ValueError):
        return "NOT_FOUND"

def main():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return

    try:
        json_data = json.loads(lines[0])
        n = int(lines[1])
        
        for i in range(2, 2 + n):
            if i < len(lines):
                print(resolve_query(json_data, lines[i].strip()))
    except (ValueError, json.JSONDecodeError):
        pass

if __name__ == "__main__":
    main()