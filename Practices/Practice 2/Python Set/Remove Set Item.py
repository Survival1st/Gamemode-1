#1 example
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

print(fruits) # {'apple', 'cherry'}

#2 example
fruits = {"apple", "banana", "cherry"}
fruits.discard("orange") # No error occurs

print(fruits) # Still {'apple', 'banana', 'cherry'}

#3 example
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()

print(x)      # 'apple', 'banana', or 'cherry'
print(fruits) 
