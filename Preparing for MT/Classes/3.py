class smartphone:
    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = 100
    def use(self):
        amount = int(input())
        self.battery_level -= amount
        return self.battery_level
    def charge(self):
        self.battery_level = 100
        return self.battery_level
    def status(self):
        return self.battery_level
my_phone = smartphone("jarvice", "100")
print(my_phone.name)
print(my_phone.use())  
print(my_phone.status())  
print(my_phone.charge())