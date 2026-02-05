#1 example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])  # Ford

#2 example
# Method 1: 
print(thisdict["brand"]) # Ford

# Method 2: get() method
print(thisdict.get("model")) # Mustang