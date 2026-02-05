#1 example
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}

myfamily = {
  "child1": child1,
  "child2": child2
}

#2 example
for name, info in myfamily.items():
    print(f"ID: {name}")
    for key in info:
        print(f"{key}: {info[key]}")

#3 example
print(myfamily["child2"]["name"]) # Tobias