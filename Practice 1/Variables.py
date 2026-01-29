#1 example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#2 example
x = 5
y = "John"
print(type(x))
print(type(y))

#3 example
#2myvar = "John"
#my-var = "John"
#my var = "John"
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#4 example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#5 example
x = y = z = "Orange"
print(x)
print(y)
print(z)

#6 example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#7 example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#8 example
"""x = 5
y = "John"
print(x + y)"""
x = 5
y = "John"
print(x, y)

#9 example
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#10 example
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#11 example
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)