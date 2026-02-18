# Example 1
def get_dimensions(radius):
    diameter = 2 * radius
    circumference = 2 * 3.14159 * radius
    area = 3.14159 * (radius ** 2)
    return diameter, circumference, area

d, c, a = get_dimensions(5)
print(f"D: {d}, C: {c}, A: {a}")
# this will print the diameter, circumference, and area of a circle with radius 5

# Example 2
def process_payment(balance, amount):
    if amount <= 0:
        return "Invalid amount"
    
    if balance < amount:
        return "Insufficient funds"
    
    new_balance = balance - amount
    return f"Success! New balance: {new_balance}"

print(process_payment(100, -50))
print(process_payment(100, 20))
print(process_payment(100, 150))
# this will demonstrate the function's behavior with different payment amounts

# Example 3
def power_factory(exponent):
    def calculate(base):
        return base ** exponent
    return calculate

square = power_factory(2)
cube = power_factory(3)

print(square(5))
print(cube(5))
# this will create two functions, one for squaring and one for cubing a number, and then demonstrate their usage