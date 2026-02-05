#1 example of Boolean values in Python
x = 30
y = 20

''' These expressions evaluate to a Boolean
value (True or False) 
based on the comparison of x and y.'''
is_greater = x > y   # False
is_equal = x == 10   # True

print(f"Is x greater than y? {is_greater}")


#2 example of Boolean operations
a = True
b = False
and_result = a and b  # False
or_result = a or b    # True
not_result = not a     # False
print(f"AND result: {and_result}, OR result: {or_result}, NOT result: {not_result}")



#3 example of Boolean in conditional statements
is_logged_in = True

if is_logged_in:
    print("Welcome back Humanous!")
else:
    print("Please log in to continue.")

#4 example of Boolean in loops
banned_users = ["Monkey_luck", "troll_99", "hacker_jack"]
current_user = "Monkey_luck"

is_banned = current_user in banned_users

if is_banned:
    print("Access Denied.") 


#5 example of Boolean functions
cart = [] # Empty shopping cart
if not cart:
    print("Your shopping cart is empty!")