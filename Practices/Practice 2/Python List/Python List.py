#1 example
fruits = ["apple", "banana", "cherry"]
mixed = [1, "Hello", 3.14, True] # List with different data types
empty = [] # Empty list

#2 example
numbers = [10, 20, 30, 40, 50]

print(numbers[0])   # 10 (first element)
print(numbers[-1])  # 50 (last element)
print(numbers[1:4]) # [20, 30, 40] (from 1st to 4th not including)
print(numbers[::-1]) # [50, 40, 30, 20, 10] (reversed list)

#3 example
# Adding elements
squares = [x**2 for x in range(10) if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]

#4 example
