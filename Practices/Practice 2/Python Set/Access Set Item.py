#1 example 
fruits = {"apple", "banana", "cherry"}

print("banana" in fruits) # Returns True
print("orange" in fruits) # Returns False

#2 example
colors = {"red", "green", "blue"}

for color in colors:
    print(color)

#3 example
letters = {"a", "b", "c"}
removed_item = letters.pop()

print(removed_item) # Could be 'a', 'b', or 'c'
print(letters)      # The remaining two items