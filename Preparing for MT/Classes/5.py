class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Some sound"
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"  
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")
