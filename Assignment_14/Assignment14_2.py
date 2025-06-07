class rectangle:

    def __init__(self, A, B):
        self.length = A
        self.width = B

    def area(self):
        ret=self.length*self.width
        print("area of rectangle: ",ret)

    def perimeter(self):
        ret=2*(self.length+self.width)
        print("perimeter of rectangle: ",ret)
        
def main():
    obj1=rectangle(10,5)

    obj1.area()
    obj1.perimeter()

if __name__ == "__main__":
    main()