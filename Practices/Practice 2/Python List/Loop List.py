#1 example
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

#2 example
numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 10

print(numbers) # [10, 20, 30, 40]

#3 example
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Цвет №{index}: {color}")

#4 example
cars = ["Toyota", "Mazda", "Hyundai"]
i = 0

while i < len(cars):
    print(cars[i])
    i += 1
    