# Example 1
numbers = int(input())
squares = (x**2 for x in range(1, numbers + 1))

for val in squares:
    print(val)

# Example 2
num = int(input())
evens = (x for x in range(1, num+1) if x%2==0)
for el in evens:
    print(el)

# Example 3
num = int(input())
q = (x for x in range(1, num+1) if x%3==0 or x%4==0)
for i in q:
    print(i)