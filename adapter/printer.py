class Printer:
    def __init__(self, obj):
        self.obj = obj

    def print_weak(self):
        self.obj.print_weak()

    def print_strong(self):
        self.obj.print_strong()

class OldPrinter:
    def __init__(self, string):
        self.string = string

    def show_with_paren(self):
        print("({0})".format(self.string))

    def show_with_astr(self):
        print("*{0}*".format(self.string))

class Adapter:
    def __init__(self, string):
        self.old_printer = OldPrinter(string)

    def print_weak(self):
        self.old_printer.show_with_paren()

    def print_strong(self):
        self.old_printer.show_with_astr()

def main():
    p = Printer(Adapter("Hello"))
    p.print_weak()
    p.print_strong()

if __name__ == "__main__":
    main()

