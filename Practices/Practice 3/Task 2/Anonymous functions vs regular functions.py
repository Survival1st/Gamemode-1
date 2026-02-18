# Example 1
# Regular Function
def get_status(age):
    if age < 18:
        return "Minor"
    return "Adult"

# Lambda equivalent (using ternary operator)
status_lambda = lambda age: "Minor" if age < 18 else "Adult"

# Example 2
# Using a regular function for sorting
def second_item(x):
    return x[1]

pairs = [(1, 10), (2, 5), (3, 8)]
pairs.sort(key=second_item)

# Using a lambda (Cleaner for simple cases)
pairs.sort(key=lambda x: x[1])

