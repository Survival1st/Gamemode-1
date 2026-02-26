import json

json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)

print(data["name"])