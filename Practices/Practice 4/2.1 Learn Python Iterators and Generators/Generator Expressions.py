# Example 1
numbers = [1, 2, 3, 4, 5]
squares = (x**2 for x in numbers)

for val in squares:
    print(val)

# Example 2
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
short_names_upper = (n.upper() for n in names if len(n) <= 4)

for name in short_names_upper:
    print(name)

# Example 3
def get_raw_data():
    return (i for i in range(1000000))

raw_data = get_raw_data()
filtered_data = (x for x in raw_data if x % 3 == 0)
final_results = (f"Value: {val}" for val in filtered_data if "9" in str(val))

for _ in range(5):
    print(next(final_results))