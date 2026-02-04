#1 example
numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n**2)

#2 example
squares = [n**2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

#3 example
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in nums if x % 2 == 0]
# Result: [2, 4, 6, 8, 10]

#4 example
results = [x if x % 2 == 0 else "Odd" for x in range(5)]
# Result: [0, 'Odd', 2, 'Odd', 4]

