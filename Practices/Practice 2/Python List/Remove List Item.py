#1 example
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana") 
print(fruits) # ['apple', 'cherry', 'banana'] —  "banana" removed only from the first occurrence

#2 example
letters = ["a", "b", "c", "d"]
removed_item = letters.pop(1) # Delete "b" (index 1)

print(letters)      # ['a', 'c', 'd']
print(removed_item) # 'b'

#3 example
numbers = [10, 20, 30, 40, 50, 60]

del numbers[0]    
del numbers[1:3]   
print(numbers)     

#4 example
nums = [1, 2, 3, 2, 4, 2, 5]
# Using list comprehension to remove all occurrences of 2
nums = [x for x in nums if x != 2]
print(nums) # [1, 3, 4, 5]

#5 example
colors = ["red", "green", "blue"]
colors.clear()
print(colors) # []