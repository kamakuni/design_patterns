class AbstractDisplay:

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()
