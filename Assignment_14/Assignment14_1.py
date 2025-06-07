class employee:

    def __init__(self, A, B, C):
        self.name = A
        self.salary = B
        self.employeeID = C

    def display(self):
        print("Name: "+self.name)
        print("salary: ",self.salary)
        print("ID: ",self.employeeID)
        
def main():
    obj1=employee("Rohit",50000,101)

    obj1.display()

if __name__ == "__main__":
    main()