#1 example
user = {
    "username": "coder123",
    "email": "abc@example.com",
    "level": 5
}

print(user["username"])  # coder123

#2 example
status = user.get("status") 
print(status)  
status = user.get("status", "Offline")
print(status)  # Offline

#3 example
car = {"brand": "Tesla", "model": "S", "year": 2023}

print(car.keys())   
print(car.values()) 
print(car.items())  