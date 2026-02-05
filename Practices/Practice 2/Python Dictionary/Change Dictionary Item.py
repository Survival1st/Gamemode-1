#1 example
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["year"] = 2024 
print(car)

#2 example
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"year": 2020, "color": "red"})
print(car)

#3 example
user = {"name": "Alice"}
user["age"] = 30 
print(user) # {'name': 'Alice', 'age': 30}