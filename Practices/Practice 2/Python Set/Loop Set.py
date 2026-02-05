#1 example
fruits = {"apple", "banana", "cherry"}

for x in fruits:
    print(x)

#2 example
colors = {"red", "green", "blue"}

for count, color in enumerate(colors, start=1):
    print(f"Color {count}: {color}")

#3 example
numbers = {1, 2, 3, 4, 5}
squares = {x**2 for x in numbers if x % 2 == 0}
print(squares) # {16, 4}