# Example 1
class User:
    def __init__(self, username, status):
        self.username = username
        self.status = status

user1 = User("Alice", "Offline")
user1.status = "Online"
print(f"{user1.username} is now {user1.status}")

# Example 2
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_phone = Smartphone("Apple", "iPhone 15")
setattr(my_phone, "model", "iPhone 16 Pro")
print(f"Updated Model: {my_phone.model}")

# Example 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.temporary_note = "Available for 24h"

book1 = Book("1984", "George Orwell")
del book1.temporary_note
try:
    print(book1.temporary_note)
except AttributeError:
    print("The property 'temporary_note' no longer exists.")