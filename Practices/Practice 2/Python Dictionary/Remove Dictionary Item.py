#1 example
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

removed_value = car.pop("model")

print(car)           # {'brand': 'Ford', 'year': 1964}
print(removed_value) # Mustang

#2 example
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
print(car) # {'brand': 'Ford', 'model': 'Mustang'}

#3 example
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del car["brand"]
del car 
