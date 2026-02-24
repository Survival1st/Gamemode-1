# Example 1
import os
import json

filename = "data.json"
if os.path.exists(filename):
    with open(filename, "r") as file:
        data = json.load(file)
else:
    print(f"Error: {filename} not found!")

# Example 2
import json

with open("user_profile.json", "r") as file:
    profile = json.load(file)

# Navigating nested keys
username = profile["user"]["username"]
first_skill = profile["user"]["skills"][0]

print(f"User: {username}, Skill: {first_skill}")

# Example 3
import json

def load_config(filepath):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' does not exist.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: '{filepath}' contains invalid JSON.")
        return {}

config = load_config("settings.json")
theme = config.get("theme", "default-light")
print(f"Active Theme: {theme}")