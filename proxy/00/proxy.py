import getpass

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class AccountError(Exception):
    pass

class BankAccountProxy:
    def __init__(self, real_object, owner_name):
        self.real_object = real_object
        self.owner_name = owner_name

    def balance(self):
        self.__check_access()
        self.real_object.balance

    def deposit(self, amount):
        self.__check_access()
        self.real_object.deposit(amount)

    def withdraw(self, amount):
        self.__check_access()
        self.real_object.withdraw(amount)

    def __check_access(self):
        if(getpass.getuser() != self.owner_name):
            raise AccountError("Illegal access: {0} cannot access account.".format(self.owner_name))


account = BankAccount(100)
proxy = BankAccountProxy(account, "kenMBA")
print(proxy.deposit(50))
print(proxy.withdraw(10))

account = BankAccount(100)
proxy = BankAccountProxy(account, "no_login_user")
print(proxy.deposit(50))
print(proxy.withdraw(10))