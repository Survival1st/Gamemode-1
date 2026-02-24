# Example 1
{
  "name": "John",
  "age": 30,
  "is_student": False,
  "skills": ["Python", "SQL"]
}

# Example 2
import json

data = {
    "title": "Data",
    "active": True,
    "limit": None,
    "coords": (10, 20)
}


json_output = json.dumps(data)
print(json_output)

# Example 3
import json


raw_json = """
{
    "office": {
        "medical": [
            {"room": 101, "status": "available"},
            {"room": 102, "status": "occupied"}
        ],
        "parking": null
    }
}
"""

data = json.loads(raw_json)
print(data["office"]["medical"][0]["room"])
