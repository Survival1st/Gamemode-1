# Example 1
class Camera:
    def take_photo(self):
        print("Photo taken!")

class Phone:
    def make_call(self):
        print("Calling...")
class Smartphone(Camera, Phone):
    pass

my_phone = Smartphone()
my_phone.take_photo()
my_phone.make_call()

# Example 2
class Logger:
    def log(self):
        print("Logging to a text file.")

class Database:
    def log(self):
        print("Logging to the database.")
class App(Logger, Database):
    def run(self):
        print("App is running...")
        self.log() 

my_app = App()
my_app.run() 

# Example 3
class FlyingMixin:
    def fly(self):
        print(f"{self.name} is flying high!")

class SwimmingMixin:
    def swim(self):
        print(f"{self.name} is swimming fast!")

class Animal:
    def __init__(self, name):
        self.name = name

class Duck(Animal, FlyingMixin, SwimmingMixin):
    pass

class Penguin(Animal, SwimmingMixin):
    pass

donald = Duck("Donald")
donald.fly()
donald.swim()