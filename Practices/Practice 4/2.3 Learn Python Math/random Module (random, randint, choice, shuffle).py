# Example 1
import random

print(random.random())
print(random.randint(1, 10))
print(random.randrange(0, 100, 5))

# Example 2
import random

colors = ["red", "blue", "green", "yellow", "purple"]

picked = random.choice(colors)
print(f"Single pick: {picked}")

random.shuffle(colors)
print(f"Shuffled list: {colors}")

multiple = random.sample(colors, k=2)
print(f"Unique sample: {multiple}")

# Example 3
import random

random.seed(42)
print(f"Consistent result 1: {random.random()}")

random.seed(42)
print(f"Consistent result 2: {random.random()}")

print(f"Normal distribution: {random.gauss(0, 1)}")

weights = [10, 80, 10]
items = ["Low", "High", "Low"]
weighted_pick = random.choices(items, weights=weights, k=5)
print(f"Weighted results: {weighted_pick}")