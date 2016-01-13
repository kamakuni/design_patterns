import time 

class Image(object):
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        __load_image_from_disk()

    def __load_image_from_disk(self, filename):
        print("loading "+filename+" begin")
        time.sleep(100)
        print("loading "+filename+" end")

    def display(self):
        print("Displaying "+self.filename)

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.image = None
        #if image == None:
        #    image = RealImage(filename)
        #image.display()

def main():
    image1 = ProxyImage("filename1")    
    image2 = ProxyImage("filename2")
    image3 = ProxyImage("filename3")

    image1.display()
    image2.display()
    image3.display()


if __name__ == "__main__":
    main()