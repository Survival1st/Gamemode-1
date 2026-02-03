x = 24
y = 5
z = 7

# Addition
add_result = x + y + z
print(f"Addition: {x} + {y} + {z} = {add_result}")

# Subtraction
sub_result = x - y - z
print(f"Subtraction: {x} - {y} - {z} = {sub_result}")

# Multiplication
mul_result = x * y * z
print(f"Multiplication: {x} * {y} * {z} = {mul_result}")

# Division
div_result = x / y
print(f"Division: {x} / {y} = {div_result}")

# Floor Division
floor_div_result = x // y
print(f"Floor Division: {x} // {y} = {floor_div_result}")

# Modulus
mod_result = x % y
print(f"Modulus: {x} % {y} = {mod_result}")

# Exponentiation
exp_result = y ** z
print(f"Exponentiation: {y} ** {z} = {exp_result}")

# Combined Operations
combined_result = (x + y) * z / (y - 2) ** 2
print(f"Combined Operations: ({x} + {y}) * {z} / ({y} - 2) ** 2 = {combined_result}")

# Using parentheses to change precedence
parentheses_result = x + (y * z)
print(f"Using Parentheses: {x} + ({y} * {z}) = {parentheses_result}")

# Incrementing and Decrementing
x += 5
print(f"After Incrementing by 5: x = {x}")
y -= 2
print(f"After Decrementing by 2: y = {y}")
z *= 3
print(f"After Multiplying by 3: z = {z}")
z /= 2
print(f"After Dividing by 2: z = {z}")

# Mixing different operators
mix_result = (x % y) + (z ** 2) - (x // z)
print(f"Mixing Different Operators: ({x} % {y}) + ({z} ** 2) - ({x} // {z}) = {mix_result}")

# Using variables in expressions
final_result = (add_result + mul_result) / (sub_result + div_result)
print(f"Final Result using previous results: ({add_result} + {mul_result}) / ({sub_result} + {div_result}) = {final_result}")

