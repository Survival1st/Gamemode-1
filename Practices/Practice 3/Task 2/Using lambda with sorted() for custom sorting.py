# Example 1
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 300}
]
cheapest_first = sorted(products, key=lambda x: x["price"])
print(cheapest_first)
# this code sorts the list of products by their price in ascending order using a lambda function as the key. The sorted list is then printed, showing the products ordered from cheapest to most expensive.

# Example 2
students = [("Alice", "B"), ("Bob", "A"), ("Charlie", "C")]
by_grade = sorted(students, key=lambda student: student[1])
print(by_grade)
# In this example, we have a list of tuples representing students and their grades. We use the sorted function with a lambda as the key to sort the students by their grade (the second element of each tuple). The sorted list is printed, showing the students ordered by their grades.

# Example 3
words = ["banana", "apple", "cherry", "kiwi", "fig"]
complex_sort = sorted(words, key=lambda x: (len(x), x))
print(complex_sort)
# this code sorts the list of words first by their length, and then alphabetically for words of the same length. The sorted list is printed.

# Example 4
expensive_first = sorted(products, key=lambda x: x["price"], reverse=True)
print(expensive_first)
# Here, we sort the list of products by their price in descending order by setting the reverse parameter to True. The sorted list is printed, showing the products ordered from most expensive to cheapest.