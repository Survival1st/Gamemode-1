# Example 1
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print(data)

# Example 2
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)


for record in data["records"]:
    name = record.get("name", "N/A")
    value = record.get("value", 0)
    print(f"Record: {name} | Value: {value}")

# Example 3
import json

def process_json_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        
        
        active_items = [item for item in data if item.get("status") == "active"]
        total_sum = sum(item.get("amount", 0) for item in active_items)
        
        return {
            "count": len(active_items),
            "total_amount": total_sum,
            "names": [item["name"] for item in active_items]
        }
        
    except FileNotFoundError:
        return "Error: File not found."
    except json.JSONDecodeError:
        return "Error: Failed to decode JSON."

result = process_json_data("sample-data.json")
print(result)
