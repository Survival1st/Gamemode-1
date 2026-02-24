# Example 1
import json

data = {"name": "Alice", "role": "Admin"}

with open("user.json", "w") as file:
    json.dump(data, file)

# Example 2
import json

config = {
    "version": 1.0,
    "debug": True,
    "permissions": ["read", "write", "execute"]
}

with open("config.json", "w") as file:
    json.dump(config, file, indent=4, sort_keys=True)

# Example 3
import json
import os

def update_json_list(filename, new_item):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(new_item)

    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

update_json_list("log.json", {"event": "login", "id": 501})
update_json_list("log.json", {"event": "logout", "id": 501})

