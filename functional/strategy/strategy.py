def main():
    add = lambda a,b: a + b
    subtract = lambda a,b: a - b
    multiply = lambda a,b: a * b
    execute = lambda callback,x,y:callback(x,y)

    print(execute(add,3,3))
    print(execute(subtract,3,3))
    print(execute(multiply,3,3))

if __name__ == "__main__":
    main()
