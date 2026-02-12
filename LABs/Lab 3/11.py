class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        return self.a + other.a, self.b + other.b

data = list(map(int, input().split()))
p1 = Pair(data[0], data[1])
p2 = Pair(data[2], data[3])

sum_a, sum_b = p1.add(p2)

print(f"Result: {sum_a} {sum_b}")