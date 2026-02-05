#1 example
thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)

#2 example
thistuple = ("apple", "banana", "cherry")

for i in range(len(thistuple)):
    print(f"Index {i}: {thistuple[i]}")

#3 example
thistuple = ("apple", "banana", "cherry")

for index, value in enumerate(thistuple):
    print(f"Item {index} is {value}")
    