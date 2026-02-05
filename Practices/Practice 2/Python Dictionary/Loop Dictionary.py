#1 example
user = {"name": "Alice", "age": 25, "role": "Admin"}

for key in user:
    print(key) 

#2 example
for val in user.values():
    print(val)

#3 example
for key, value in user.items():
    print(f"The {key} is {value}")

#4 example
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
discount_prices = {k: v * 0.9 for k, v in prices.items()}
print(discount_prices) 