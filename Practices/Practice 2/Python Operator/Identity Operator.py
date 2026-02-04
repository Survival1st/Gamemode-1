#1 example
a = [1, 2, 3]
b = a          
c = [1, 2, 3]  

print(a is b)  
print(a is c)  

#2 example
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#3 example
x = 250
y = 250
print(x is y) 
x = 1000
y = 1000
print(x is y)