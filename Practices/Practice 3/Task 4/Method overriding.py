# Example 1
class Animal:
    def speak(self):
        print("The animal makes a generic sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks: Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("The cat meows: Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()

# Example 2
class Product:
    def __init__(self, price):
        self.price = price

    def get_final_price(self):
        return self.price

class ClearanceProduct(Product):
    def get_final_price(self):
        return self.price * 0.5

item1 = Product(100)
item2 = ClearanceProduct(100)

print(f"Normal Price: ${item1.get_final_price()}")    
print(f"Clearance Price: ${item2.get_final_price()}") 

# Example 3
class Shape:
    def draw(self):
        print("Drawing a general shape.")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle using radius and Pi.")

class Square(Shape):
    def draw(self):
        print("Drawing a square using four equal sides.")
shapes = [Circle(), Square()]
for s in shapes:
    s.draw()