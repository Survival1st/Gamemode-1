# Example 1
x = -7.5
y = 3

print(abs(x))
print(round(x))
print(pow(y, 2))

# Example 2
prices = [120, 450, 10, 89, 300]

lowest = min(prices)
highest = max(prices)

print(f"Range: {lowest} to {highest}")

val = 12.5678
print(round(val, 2))

# Example 3
users = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 70}
]

top_user = max(users, key=lambda u: u["score"])
bottom_user = min(users, key=lambda u: u["score"])

print(top_user["name"])

coords = [(1, 2), (3, 10), (5, 1)]
farthest_y = max(coords, key=lambda c: c[1])
print(farthest_y)

print(pow(10, 2, 3))