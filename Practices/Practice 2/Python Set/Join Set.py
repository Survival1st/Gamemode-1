#1 example
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set4 = set1 | set2

print(set3) # {'a', 1, 'b', 2, 'c', 3}

#2 example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z) # {'apple'}

#3 example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x - y
print(z) # {'banana', 'cherry'}