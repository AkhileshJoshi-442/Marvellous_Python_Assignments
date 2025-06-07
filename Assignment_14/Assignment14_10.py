class employee:
    def __init__(self, a,b,c):
        self.name=a          
        self._department=b           
        self.__salary=c        
    
    def display(self):
        print("name: "+self.name)
        print("department: "+self._department)
        print("salary: ",self.__salary)
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__salary = new_salary

def main():
    obj = employee('Rahul',"development",50000)

    print("name:", obj.name)
    print("department:", obj._department)
    print("salary:", obj.get_salary())

    obj.set_salary(55000)
    print("updated Salary:", obj.get_salary())
    obj.display()

if __name__=="__main__":
    main()

