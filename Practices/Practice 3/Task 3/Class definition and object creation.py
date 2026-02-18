# Example 1
class Dog:
    species = "Canine"  

    def __init__(self, name, breed):
        self.name = name    
        self.breed = breed  

    def bark(self):
        return f"{self.name} says Woof!"
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())
# This code defines a Dog class with a class attribute 'species' and instance attributes 'name' and 'breed'. The bark method returns a string indicating the dog's name and its bark. An instance of the Dog class is created and the bark method is called to display the output.

# Example 2
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")
print(dog1.name)    
print(dog2.bark())  
# this code creates two instances of the Dog class, dog1 and dog2, with different names and breeds. It then prints the name of dog1 and the bark of dog2, demonstrating how each instance can have its own unique attributes and behaviors while sharing the same class definition.

# Example 3
class Car:
    wheels = 4  

    def __init__(self, color):
        self.color = color  

my_car = Car("Red")
print(my_car.wheels) 
print(my_car.color)  
# This code defines a Car class with a class attribute 'wheels' and an instance attribute 'color'. An instance of the Car class is created with the color "Red". The code then prints the number of wheels (which is a class attribute) and the color of the car (which is an instance attribute).