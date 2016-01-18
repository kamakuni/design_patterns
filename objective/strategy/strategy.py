def main():
    strategies = [Add(), Multiply()]
    for strategy in strategies:
        print(strategy.product(2,3))

class Calc:
    def product(self):
        pass

class Add(Calc):
    def product(self,m,n):
        return m + n

class Multiply(Calc):
    def product(self,m,n):
        return m * n

if __name__ == "__main__":
    main()