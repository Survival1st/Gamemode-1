# Correct Email 
import re
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|kz)"
user = input()
if(re.search(pattern, user)):
    print("Valid Email")
else:
    print("Invalid Email")
    