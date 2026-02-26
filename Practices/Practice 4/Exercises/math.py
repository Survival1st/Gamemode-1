# Example 1
import math
a = int(input("Degree: "))
print("Radian: ", math.radians(a))

# Example 2
def calculate_trapezoid_area(base1, base2, height):
    return ((base1 + base2) / 2) * height

a = float(input("Enter length of base 1: "))
b = float(input("Enter length of base 2: "))
h = float(input("Enter the height: "))
area = calculate_trapezoid_area(a, b, h)
print(f"The area of the trapezoid is: {area}")

# Example 3
import math

def regular_polygon_area(n, s):
    numerator = n * (s ** 2)
    denominator = 4 * math.tan(math.pi / n)
    return numerator / denominator
n_sides = int(input("Enter the number of sides: "))
side_length = float(input("Enter the length of one side: "))
area = regular_polygon_area(n_sides, side_length)
print(f"The area of the {n_sides}-sided polygon is: {area:.4f}")