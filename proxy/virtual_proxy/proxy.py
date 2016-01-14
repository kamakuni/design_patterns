class BankAccount:

    def __init__(self, balance):
        print("bank account is generated")
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class VirtualAccountProxy:

    def __init__(self, starting_balance):
        print("virtual account proxy is generated")
        self.subject = None
        self.starting_balance = starting_balance

    def balance(self):
        self.create()
        self.subject.balance

    def deposit(self, amount):
        self.create()
        self.subject.deposit(amount)

    def withdraw(self, amount):
        self.create()
        self.subject.withdraw(amount)

    def announce(self):
        return "virtual account proxy is announcing"

    def create(self):
        if self.subject is None:
            self.subject = BankAccount(self.starting_balance)

def main():
    proxy = VirtualAccountProxy(100)
    print(proxy.announce())
    proxy.deposit(50)
    proxy.withdraw(10)

if __name__ == "__main__":
    main()