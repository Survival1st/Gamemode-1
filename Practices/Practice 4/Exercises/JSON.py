import json
try:
    with open('sample-data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: File sample-data.json not found.")
    exit()

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 50, "-" * 20, "-" * 7, "-" * 6)

for item in data.get('imdata', []):
    if 'l1PhysIf' in item:
        attributes = item['l1PhysIf']['attributes']
        dn = attributes.get('dn', '')
        descr = attributes.get('descr', '')
        speed = attributes.get('speed', 'inherit')
        mtu = attributes.get('mtu', '')
        
        print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")