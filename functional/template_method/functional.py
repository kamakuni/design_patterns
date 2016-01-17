class CustomerBlocks:

    def __init__(self):
        self.checkCredit
        self.checkInventory
        self.ship

    def process(self):
        self.checkCredit()
        self.checkInventory()
        self.ship()

class MyCustomerBlocks(CustomerBlocks):

    def __init__(self):
        self.checkCredit = lambda : print("my customer checks credit")
        self.checkInventory = lambda : print("my customer checks inventory")
        self.ship = lambda : print("my customer ships")

#class MyCustomer(Customer):

#    def checkCredit(self):
#        print("my customer checks credit")

#    def checkInventory(self):
#        print("my customer checks inventory")

#    def ship(self):
#        print("my customer ships")

def main():
    customer = MyCustomerBlocks()
    customer.process()

if __name__ == "__main__":
    main()
    
    