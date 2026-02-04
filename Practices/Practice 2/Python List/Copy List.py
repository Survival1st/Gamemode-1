#1 example
original = ["apple", "banana", "cherry"]
clone = original.copy()

clone.append("orange")

print(original) # ['apple', 'banana', 'cherry']
print(clone)    # ['apple', 'banana', 'cherry', 'orange']

#2 example
original = [1, 2, 3]
clone = list(original)
clone.remove(2)
print(original) # [1, 2, 3]
print(clone)    # [1, 3]

#3 example
original = ["A", "B", "C"]
clone = original[:]
clone[0] = "Z"
