# Example 1
prices_usd = [10.99, 25.00, 5.50, 100.00]
exchange_rate = 0.92
prices_eur = list(map(lambda p: round(p * exchange_rate, 2), prices_usd))

print(prices_eur)
# this code will output: [10.07, 23.0, 5.06, 92.0]

# Example 2
players = [
    {"name": "Alice", "score": 100, "time": 45},
    {"name": "Bob", "score": 100, "time": 30},
    {"name": "Charlie", "score": 85, "time": 20}
]
ranked = sorted(players, key=lambda p: (-p["score"], p["time"]))

print(ranked)
# this code will output: [{'name': 'Bob', 'score': 100, 'time': 30}, {'name': 'Alice', 'score': 100, 'time': 45}, {'name': 'Charlie', 'score': 85, 'time': 20}]

# Example 3
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))
print(triple(10))
# this code defines a function make_multiplier that takes a number n and returns a lambda function that multiplies its input by n. We create two multiplier functions, double and triple, and then call them with the argument 10. The output will be:

# Example 4
numbers = [1, 12, 5, 20, 7, 15]
filtered_list = list(filter(lambda x: x % 2 == 0 and x > 10, numbers))

print(filtered_list)
# this code will output: [12, 20, 15]