# Example 1
fruits = ["apple", "banana", "cherry"]
my_it = iter(fruits)
print(next(my_it))  
print(next(my_it))  
print(next(my_it))  

# Example 2
word = "Code"
it = iter(word)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Example 3
numbers = [1, 2, 3]
it = iter(numbers)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
    