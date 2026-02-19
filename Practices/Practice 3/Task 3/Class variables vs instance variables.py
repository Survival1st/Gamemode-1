# Example 1
class Enemy:
    difficulty_level = "Hard"

    def __init__(self, name, health):
        self.name = name
        self.health = health

grunt = Enemy("Grunt", 50)
boss = Enemy("MegaBoss", 500)
Enemy.difficulty_level = "Legendary"

print(f"{grunt.name} is on {grunt.difficulty_level} mode.") 
print(f"{boss.name} is on {boss.difficulty_level} mode.")   

# Example 2
class Car:
    total_cars_created = 0

    def __init__(self, model):
        self.model = model
        Car.total_cars_created += 1

car1 = Car("Tesla")
car2 = Car("Ford")
car3 = Car("Toyota")

print(f"Total cars in the fleet: {Car.total_cars_created}")
print(f"{car1.model} sees {car1.total_cars_created} total cars.")

# Example 3
class Item:
    discount_rate = 0.10 

    def __init__(self, price):
        self.price = price 

bread = Item(5.00)
milk = Item(3.00)
Item.discount_rate = 0.20 
print(bread.discount_rate) 
bread.discount_rate = 0.50 

print(bread.discount_rate) 
print(milk.discount_rate)