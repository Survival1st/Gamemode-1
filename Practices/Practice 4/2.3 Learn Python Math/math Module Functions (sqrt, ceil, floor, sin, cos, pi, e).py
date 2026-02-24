# Example 1
import math

print(math.pi)
print(math.e)

print(math.sqrt(64))
print(math.isqrt(65))

# Example 2
import math

val = 4.2

print(math.ceil(val))
print(math.floor(val))
print(math.trunc(-4.9))

print(math.pow(2, 3))
print(math.log(100, 10))

# Example 3
import math

angle_deg = 45
angle_rad = math.radians(angle_deg)

print(math.sin(angle_rad))
print(math.cos(angle_rad))


point1 = (0, 0)
point2 = (3, 4)
distance = math.dist(point1, point2)

print(f"Distance: {distance}")
print(f"Factorial of 5: {math.factorial(5)}")