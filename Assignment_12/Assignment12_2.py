class circle:
    pi = 3.142

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
        
    def accept(self):
        print("enter radius: ")
        self.radius=int(input())

    def calculateArea(self):
        self.area= circle.pi*self.radius**2

    def calculateCircumference(self):
        self.circumference= circle.pi*self.radius*2

    def display(self):
        print("radius of circle: ",self.radius)
        print("area of circle: ",self.area)
        print("cicumference of circle: ",self.circumference)

def main():
    obj1 = circle()

    obj1.accept()
    obj1.calculateArea()
    obj1.calculateCircumference()
    obj1.display()
    
if __name__ == "__main__":
    main()