# Example 1
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"The {self.brand} engine is starting...")

class Car(Vehicle):
    def drive(self):
        print(f"The {self.brand} is driving on the road.")

my_car = Car("Toyota")
my_car.start_engine()  
my_car.drive()         

# Example 2
class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks!")

class Cat(Animal):
    def speak(self):
        print("The cat meows!")

dog = Dog()
cat = Cat()

dog.speak()  
cat.speak()  

# Example 3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        print(f"{self.name} manages the {self.department} dept.")

mgr = Manager("Alice", 90000, "IT")
mgr.show_info()
