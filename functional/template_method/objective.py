from abc import ABCMeta
from abc import abstractmethod

class Customer(metaclass=ABCMeta):

    def __init__(self):
        self.plan = []

    @abstractmethod
    def checkCredit(self):
        pass

    @abstractmethod
    def checkInventory(self):
        pass

    @abstractmethod
    def ship(self):
        pass

    def process(self):
        self.checkCredit()
        self.checkInventory()
        self.ship()

class MyCustomer(Customer):

    def checkCredit(self):
        print("my customer checks credit")

    def checkInventory(self):
        print("my customer checks inventory")

    def ship(self):
        print("my customer ships")

def main():
    customer = MyCustomer()
    customer.process()

if __name__ == "__main__":
    main()
    
    