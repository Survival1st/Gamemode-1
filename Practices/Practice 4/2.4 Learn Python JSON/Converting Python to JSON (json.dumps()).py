# Example 1
import json

user = {"name": "Alice", "active": True}
json_string = json.dumps(user)

print(json_string)

# Example 2
import json

data = {
    "id": 101,
    "colors": ["red", "blue"],
    "status": None,
    "verified": False
}

formatted_json = json.dumps(data, indent=4, sort_keys=True)
print(formatted_json)

# Example 3
import json
from datetime import datetime

def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

data = {
    "timestamp": datetime.now(),
    "unique_ids": {10, 20, 30},
    "message": "Update"
}

json_output = json.dumps(data, default=custom_serializer)
print(json_output)