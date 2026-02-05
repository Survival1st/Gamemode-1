#1 example
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#2 example
for char in "Python":
    print(char)

#3 example
# Loops from 0 to 4 (5 is not included)
for i in range(5):
    print(i)

# Specifying a start and end: range(start, stop)
for i in range(2, 6):
    print(i) # Output: 2, 3, 4, 5

# Specifying an increment: range(start, stop, step)
for i in range(0, 10, 2):
    print(i) # Output: 0, 2, 4, 6, 8