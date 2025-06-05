class arithmetic():

    def __init__(self):
        self.value1 = 0.0
        self.value2 = 0.0
    
    def accept(self):
        print("enter value1: ")
        self.value1=int(input())
        print("enter value2: ")
        self.value2=int(input())

    def addition(self):
        print("addition: ", self.value1+self.value2)

    def subtraction(self):
        print("addition: ", self.value1-self.value2)

    def multiplication(self):
        print("multiplication: ", self.value1*self.value2)

    def division(self):
        print("multiplication: ", self.value1/self.value2)
        
def main():
    obj1 = arithmetic()
    obj2 = arithmetic()
    obj3 = arithmetic()
    obj4 = arithmetic()

    obj1.accept()
    obj1.addition()

    obj2.accept()
    obj2.subtraction()

    obj3.accept()
    obj3.multiplication()

    obj4.accept()
    obj4.division()
    
if __name__ == "__main__":
    main()