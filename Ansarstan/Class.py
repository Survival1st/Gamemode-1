class Dog:
    def __init__(self, name, age, is_small):
        self.set_data(name, age, is_small)
        self.get_data()

    def set_data(self, name = None, age = None, is_small = None):
        self.name = name
        self.age = age
        self.is_small = is_small

    def get_data(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Маленький: {self.is_small}")


dog1 = Dog("Rex", 5, True)
dog1.set_data("John", 2)
dog2 = Dog("Luel", 3, False)
dog2.set_data("Man", 5)
