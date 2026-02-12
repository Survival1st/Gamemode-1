class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14159
        return pi * (self.radius ** 2)

r = int(input())
my_circle = Circle(r)

print(f"{my_circle.area():.2f}")