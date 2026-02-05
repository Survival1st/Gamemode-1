#1 example
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)  # apple
print(yellow) # banana
print(red)    # cherry

#2 example
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)  # apple
print(yellow) # banana
print(red)    # ['cherry', 'strawberry', 'raspberry']

#3 example
person = ("John", 25, "Developer", "New York")
name, _, _, city = person
print(name, city) # John New York