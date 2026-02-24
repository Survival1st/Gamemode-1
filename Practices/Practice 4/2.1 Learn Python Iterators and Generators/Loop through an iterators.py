# Example 1
numbers = [1, 2, 3, 4]
it = iter(numbers)

for item in it:
    print(item)

# Example 2
numbers = [10, 20, 30]
my_iter = iter(numbers)

print(next(my_iter))

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

# Example 3
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        value = self.current
        self.current -= 1
        return value

for num in Countdown(3):
    print(num)