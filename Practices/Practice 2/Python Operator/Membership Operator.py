#1 example
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  
print("orange" in fruits)  
message = "Hello, world!"
print("Hello" in message) 

#2 example
banned_users = ["admin", "root", "moderator"]
user = "guest"
if user not in banned_users:
    print("accept!") 

#3 example
person = {"name": "Aida", "age": 20}

print("name" in person)   
print("Aida" in person)   
print("Aida" in person.values()) 