#1 example
car = {
  "brand": "Ford",
  "model": "Mustang"
}
car["year"] = 1964
print(car) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#2 example
user = {"name": "Alice"}
user.update({"age": 25, "city": "New York"})
print(user) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

#3 example
user = {"name": "Alice"}
user["hobbies"] = ["Reading", "Cycling", "Coding"]