# Example 1
import json

json_string = '{"name": "Alice", "age": 25}'
user_dict = json.loads(json_string)

print(user_dict["name"])
print(type(user_dict))

# Example 2
import json

json_data = '["Python", 42, true, null]'
python_list = json.loads(json_data)

print(python_list[2])
print(python_list[3])

# Example 3
import json

raw_response = '{"metadata": {"count": 1}, "results": [{"id": "A1", "valid": true}]}'

try:
    data = json.loads(raw_response)
    item_id = data["results"][0]["id"]
    print(f"Success: {item_id}")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
except (KeyError, IndexError):
    print("Structure differs from expectation")

