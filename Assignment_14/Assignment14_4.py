class student:
    schoolname = "Abhinav"

    def __init__(self, A, B):
        self.name = A
        self.roll_no = B

    def display(self):
        print("Name : ",self.name,"Roll No : ",self.roll_no,"School : ", student.schoolname)

def main():
    obj1 =student("Aniket", 10)
    obj2 =student("Riya", 11)

    obj1.display()
    obj2.display()

    student.schoolname = "KHS School"

    print("Change school name")

    obj1.display()
    obj2.display()

if __name__ == "__main__":
    main()