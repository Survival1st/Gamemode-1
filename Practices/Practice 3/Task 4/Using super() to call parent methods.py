# Example 1 
class Computer:
    def __init__(self, brand):
        self.brand = brand

class Laptop(Computer):
    def __init__(self, brand, battery_life):
        super().__init__(brand)
        self.battery_life = battery_life

my_laptop = Laptop("Dell", "10 hours")
print(f"{my_laptop.brand} has {my_laptop.battery_life} of battery.")

# Example 2
class Cleaner:
    def clean(self):
        print("Vacuuming the floors...")

class DetailedCleaner(Cleaner):
    def clean(self):
        super().clean()
        print("Mopping the floors and dusting the windows.")

pro_cleaner = DetailedCleaner()
pro_cleaner.clean()

# Example 3
class Database:
    def save(self, data):
        print(f"Saving '{data}' to the database...")

class SecureDatabase(Database):
    def save(self, data):
        print("[Log] Checking security permissions...")
        super().save(data)
        print("[Log] Save successful.")

db = SecureDatabase()
db.save("User_Profile_01")

