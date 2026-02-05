#1 example
tech_stack = ("Python", "Django", "PostgreSQL", "Docker")

print(tech_stack[0])   # 'Python'
print(tech_stack[-1])  # 'Docker' (Last element)
print(tech_stack[-2])  # 'PostgreSQL' (Second last element)

#2 example
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numbers[2:5])    # (2, 3, 4)
print(numbers[:4])     # (0, 1, 2, 3)
print(numbers[7:])     # (7, 8, 9)
print(numbers[::2])    # (0, 2, 4, 6, 8)

#3 example
colors = ("red", "green", "blue")

if "green" in colors:
    print("Green color found!")

#4 example
nested_tuple = ("Root", (10, 20), ["Admin", "User"])

print(nested_tuple[1])      # (10, 20)
print(nested_tuple[1][0])   # 10
print(nested_tuple[2][1])   # 'User'
