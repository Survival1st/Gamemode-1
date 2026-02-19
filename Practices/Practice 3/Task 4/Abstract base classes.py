# Example 1
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
c = Circle(5)
print(c.area())

# Example 2
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class Crypto(Payment):
    def process_payment(self, amount):
        print(f"Processing crypto wallet payment of ${amount}")

# Example 3
from abc import ABC, abstractmethod

class FileParser(ABC):
    @abstractmethod
    def parse(self, file_path):
        pass

class JSONParser(FileParser):
    def parse(self, file_path):
        return f"Parsing {file_path} as JSON..."

class CSVParser(FileParser):
    def parse(self, file_path):
        return f"Parsing {file_path} as CSV..."

