# Example 1
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# this code will output: [1, 4, 9, 16, 25]

# Example 2
names = ["alice", "BOB", "charlie"]
clean_names = list(map(lambda name: name.strip().capitalize(), names))
print(clean_names)
# this code will output: ['Alice', 'Bob', 'Charlie']

# Example 3
list_a = [1, 2, 3]
list_b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list_a, list_b))
print(sums)
# this code will output: [11, 22, 33]

