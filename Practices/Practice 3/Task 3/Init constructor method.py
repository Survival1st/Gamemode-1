# Example 1
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
my_phone = Smartphone("Apple", "iPhone 15")
print(f"Brand: {my_phone.brand}, Model: {my_phone.model}")
# this code defines a Smartphone class with an __init__ method that initializes the brand and model attributes. An instance of the Smartphone class is created with the brand "Apple" and model "iPhone 15", and the attributes are printed.

# Example 2
class User:
    def __init__(self, username, role="Member"):
        self.username = username
        self.role = role

user1 = User("Alice")           
user2 = User("Bob", "Admin")   
print(f"{user1.username} is a {user1.role}")
print(f"{user2.username} is a {user2.role}")
# In this code, the User class has an __init__ method that takes a username and an optional role parameter with a default value of "Member". Two instances of the User class are created: user1 with only a username (which defaults to "Member") and user2 with both a username and a specified role ("Admin"). The usernames and roles of both users are printed.

# Example 3
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
book1 = Book("1984", "George Orwell", 1949)
print(f"Title: {book1.title}, Author: {book1.author}, Year:
    {book1.year}")
# This code defines a Book class with an __init__ method that initializes the title, author, and year attributes. An instance of the Book class is created with the title "1984", author "George Orwell", and year 1949. The attributes of the book are printed in a formatted string.