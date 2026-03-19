class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

my_car = Car("Toyota", "Red")
print(my_car.brand) 
print(my_car.color)
my_car.drive()  