#1 example
vowels = frozenset(["a", "e", "i", "o", "u"])
print(vowels) 

#2 example
set_a = frozenset([1, 2, 3])
set_b = frozenset([1, 2, 3, 4, 5])

print(set_a.issubset(set_b)) # True
