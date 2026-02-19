# Example 1
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_phone = Smartphone("Apple", "iPhone 15")
print(f"Brand: {my_phone.brand}, Model: {my_phone.model}")


# Example 2
class User:
    def __init__(self, username, role="Member"):
        self.username = username
        self.role = role

user1 = User("Alice")
user2 = User("Bob", "Admin")
print(f"{user1.username} is a {user1.role}")
print(f"{user2.username} is a {user2.role}")


# Example 3
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book("1984", "George Orwell", 1949)
# В оригинале здесь была ошибка из-за переноса строки внутри f-строки
print(f"Title: {book1.title}, Author: {book1.author}, Year: {book1.year}") 