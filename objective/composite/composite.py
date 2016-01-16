class Entry:
    def get_name(self):
        pass

    def ls_entry(self, prefix):
        pass

    def remove(self):
        pass

class FileEntry(Entry):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def ls_entry(self, prefix):
        print("{0}/{1}".format(prefix,self.name))

    def remove(self):
        print("{0} is removed".format(self.name))

class DirEntry(Entry):

    def __init__(self, name):
        self.name = name
        self.dir = []

    def get_name(self):
        return self.name

    def add(self,entry):
        self.dir.append(entry)

    def ls_entry(self, prefix):
        print("{0}/{1}".format(prefix,self.get_name()))
        for entry in self.dir:
            entry.ls_entry("{0}/{1}".format(prefix,self.name))

    def remove(self):
        for entry in self.dir:
            entry.remove()  
        print("{0} is removed".format(self.name))

def main():
    root = DirEntry("root")
    tmp = DirEntry("tmp")
    tmp.add(FileEntry("conf"))
    tmp.add(FileEntry("data"))
    root.add(tmp)

    root.ls_entry("")

    root.remove()

if __name__ == "__main__":
    main()
