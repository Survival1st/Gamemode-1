import json

data = {
    "name": "Alice",
    "age": 25,
    "is_student": False
}

json_string = json.dumps(data)
print(json_string)