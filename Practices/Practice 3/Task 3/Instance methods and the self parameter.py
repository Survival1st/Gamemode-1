# Example 1
class Toaster:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False

    def toggle_power(self):
        self.is_on = not self.is_on
        status = "on" if self.is_on else "off"
        print(f"The {self.brand} toaster is now {status}.")

my_toaster = Toaster("Sunbeam")
my_toaster.toggle_power() 

# Example 2
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"New balance for {self.owner}: ${self.balance}"

account = BankAccount("Alex", 100)
print(account.deposit(50)) 

# Example 3
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def heal(self):
        self.health += 10
        print(f"{self.name} healed! Health is now {self.health}.")

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.health -= 5

player1 = Hero("Link", 100)
player2 = Hero("Ganon", 200)

player1.attack(player2) 