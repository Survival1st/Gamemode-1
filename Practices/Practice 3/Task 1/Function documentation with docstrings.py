# Example 1
def add(a, b):
    """Return the sum of two integers."""
    return a + b
# this function takes two integers as input and returns their sum. The docstring provides a brief description of the function's purpose.

# Example 2
def calculate_grade(scores, weight=1.0):
    """
    Calculates the weighted average of a list of test scores.

    Args:
        scores (list): A list of numerical grades.
        weight (float): The multiplier for the final result. Defaults to 1.0.

    Returns:
        float: The final weighted grade.
    """
    return (sum(scores) / len(scores)) * weight
# This function calculates the weighted average of a list of test scores. The docstring includes a description of the function, its arguments with their types and default values, and the return type.

# Example 3
def greet(name):
    """Print a greeting message."""
    print(f"Hello, {name}")

print(greet.__doc__)
help(greet)
# This function simply prints a greeting message. The docstring provides a brief description of the function's purpose. The __doc__ attribute and help() function can be used to access the docstring for documentation purposes.