# Example 1
def simple_generator():
    yield "First"
    yield "Second"
    yield "Third"

gen = simple_generator()

for item in gen:
    print(item)

# Example 2
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1

counter = count_up_to(5)

for number in counter:
    print(number)

# Example 3
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_sequence()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

for i in range(10):
    print(next(fib))

