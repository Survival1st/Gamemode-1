#1 example
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blackcurrant"
print(fruits) # ['apple', 'blackcurrant', 'cherry']

#2 example
numbers = [10, 20, 30, 40, 50]
numbers[1:3] = [21, 31]
print(numbers) # [10, 21, 31, 40, 50]

#3 example
colors = ["red", "blue"]
colors.insert(1, "green") # Now ["red", "green", "blue"]

#4 example
prices = [100, 200, 300]
# Applying a 10% discount to each price
discounted_prices = [p * 0.9 for p in prices]
print(discounted_prices) # [90.0, 180.0, 270.0]