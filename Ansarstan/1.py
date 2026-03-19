password = True
while password:
    password = input("Enter password: ")
    if password == "secret":    
        print("Access granted")
        break       
    else:
        print("Access denied, try again.")

            