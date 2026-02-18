# Example 1
def create_profile(name, age, city="Unknown", status="Active"):
    return {"user": name, "age": age, "location": city, "state": status}

print(create_profile("Alice", 28))
print(create_profile("Bob", 35, "New York", "Away"))
# This example demonstrates the use of default arguments in a function. The create_profile function has two required parameters (name and age) and two optional parameters (city and status) with default values. If the caller does not provide values for the optional parameters, the defaults will be used.

# Example 2
def calculate_total(tax_rate, *prices):
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)

print(calculate_total(0.05, 100, 200, 300))
print(calculate_total(0.10, 50, 15))
# This example shows how to use *args to accept a variable number of positional arguments (prices) and calculate the total cost including tax. The function sums up the prices and applies the tax rate to return the final total.

# Example 3
def tag_builder(tag_name, content, *styles, **attributes):
    style_str = f" style='{'; '.join(styles)}'" if styles else ""
    attr_str = "".join([f' {k}="{v}"' for k, v in attributes.items()])
    return f"<{tag_name}{style_str}{attr_str}>{content}</{tag_name}>"

print(tag_builder("div", "Hello", "color: red", "font-weight: bold", id="header", cls="container"))
# This example illustrates how to use both *args and **kwargs to create a flexible function that can handle various types of arguments for building an HTML tag.

