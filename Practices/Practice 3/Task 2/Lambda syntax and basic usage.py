# Example 1
add = lambda x, y: x + y
print(add(5, 3))
# this code defines a lambda function that takes two arguments x and y, and returns their sum. The function is then called with the arguments 5 and 3, and the result (8) is printed.

# Example 2
numbers = [1, 2, 3, 4, 5, 6]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(doubled)
print(evens)
# In this example, we have a list of numbers from 1 to 6. We use the map function with a lambda to create a new list called doubled, where each number is multiplied by 2. We also use the filter function with a lambda to create a new list called evens, which contains only the even numbers from the original list. The results are printed, showing the doubled values and the even numbers.

# Example 3
students = [("Alice", 22), ("Bob", 19), ("Charlie", 25)]
students.sort(key=lambda student: student[1])
print(students)
# Here, we have a list of tuples representing students and their ages. We use the sort method with a lambda function as the key to sort the students by their age (the second element of each tuple). The sorted list is then printed, showing the students ordered by age.