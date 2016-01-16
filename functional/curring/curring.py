def multiply(x, y):
    return x * y

def curried_multiply(x):
    def _curried_multiply(y):
        return x * y
    return _curried_multiply

curried_multiply2 = lambda x: lambda y: x * y

if __name__ == "__main__":
    # 6
    print(multiply(2, 3))
    # function
    print(curried_multiply(1))
    # 6
    print(curried_multiply(2)(3))
    # 6
    print(curried_multiply2(2)(3))