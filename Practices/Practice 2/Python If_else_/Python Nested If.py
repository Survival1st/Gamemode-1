#1 example
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above twenty!")
    else:
        print("but not above twenty.")

#2 example
user_exists = True
password_correct = False

if user_exists:
    print("User found...")
    if password_correct:
        print("Access granted!")
    else:
        print("Wrong password. Access denied.")
else:
    print("No such user exists.")

