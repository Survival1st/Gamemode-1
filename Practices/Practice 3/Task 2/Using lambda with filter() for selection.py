# Example 1
numbers = [1, 5, 8, 10, 13, 16, 20]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
# this code defines a list of numbers and uses the filter function with a lambda to create a new list called evens, which contains only the even numbers from the original list. The result is printed, showing the even numbers.

# Example 2
words = ["apple", "it", "banana", "sky", "orange"]
long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)
# In this example, we have a list of words. We use the filter function with a lambda to create a new list called long_words, which contains only the words that have more than 3 characters. The result is printed, showing the long words.

# Example 3
data = ["valid", "", None, "entry", False, 0, "active"]
clean_data = list(filter(lambda x: x, data))
print(clean_data)
# Here, we have a list of data that includes valid strings, empty strings, None, False, and 0. We use the filter function with a lambda to create a new list called clean_data, which contains only the truthy values from the original list. The result is printed, showing the valid entries.

