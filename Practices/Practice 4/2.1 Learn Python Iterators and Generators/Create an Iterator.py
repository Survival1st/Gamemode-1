# Example 1
data = [7, 8, 9]
my_iterator = iter(data)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Example 2
def sequence(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

my_seq = sequence(3)

for num in my_seq:
    print(num)

# Example 3
class PowerOfTwo:
    def __init__(self, max_exponent):
        self.max = max_exponent
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            result = 2 ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration

powers = PowerOfTwo(4)
for val in powers:
    print(val)

