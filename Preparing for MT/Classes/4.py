class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Warrior:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon

    def attack(self, target):
        target.health -= self.weapon.damage
        print(f"{self.name} ударил {target.name} мечом {self.weapon.name}!")
        print(f"У {target.name} осталось {target.health} HP.\n")


sword = Weapon("Excalibur", 25)


warrior1 = Warrior("Aragorn", sword)
warrior2 = Warrior("Legolas", sword)


warrior1.attack(warrior2)
warrior1.attack(warrior2)