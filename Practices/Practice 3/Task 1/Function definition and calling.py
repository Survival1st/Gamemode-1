#function is a reusable block of code that performs a specific task. It only runs when it is "called." Functions help break down complex programs into smaller, modular, and more manageable pieces.
# Example 1
def find_max(elements):
    if not elements:
        return None
    res = elements[0]
    for x in elements:
        if x > res:
            res = x
    return res  #This function takes a list of elements and returns the maximum value. It first checks if the list is empty and returns None if it is. Then it initializes a variable res with the first element of the list and iterates through the list, updating res whenever it finds a larger value. Finally, it returns the maximum value found.

# Example 2
def find_min(elements):
    if not elements:
        return None
    res = elements[0]
    for x in elements:
        if x < res:
            res = x
    return res   #This function is similar to find_max but instead finds the minimum value in the list. It also checks for an empty list and returns None if it is empty. It initializes res with the first element and iterates through the list, updating res whenever it finds a smaller value. Finally, it returns the minimum value found.

# Example 3
def find_average(elements):
    if not elements:
        return 0
    return sum(elements) / len(elements)  #This function calculates the average of a list of elements. It first checks if the list is empty and returns 0 if it is. Then it uses the built-in sum() function to calculate the total of the elements and divides it by the length of the list using len() to get the average.

# Example 4
def calculate_area(width, height):
    area = width * height
    return area
result = calculate_area(5, 10)
print(result)  #This function calculates the area of a rectangle given its width and height. It multiplies the width and height to get the area and returns it. The function is then called with the arguments 5 and 10, and the result is printed, which outputs 50.