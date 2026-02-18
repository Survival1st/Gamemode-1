# Example 1
def add_item(my_list):
    my_list.append("New Item")

data = ["A", "B"]
add_item(data)
print(data)  
# this will print: ['A', 'B', 'New Item']

# Example 2
def increment(number):
    number += 1
    return number

count = 10
new_count = increment(count)
print(count)     
print(new_count)  
# this will print: 10 and then 11, showing that the original count variable was not modified

# Example 3
def remove_last(items):
    items.pop()

original_list = [1, 2, 3]
remove_last(original_list[:]) 
print(original_list)
# this will print: [1, 2, 3], showing that the original list was not modified because we passed a copy of it to the function