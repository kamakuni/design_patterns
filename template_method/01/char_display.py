from abstract_display import AbstractDisplay

class CharDisplay(AbstractDisplay):

    def __init__(self, char):
        self.__char = char

    def open(self):
        print("<<")

    def print(self):
        print(self.__char)

    def close(self):
        print(">>")