class bookstore:
    noofbooks = 0

    def __init__(self,a,b):
        self.name = a
        self.author = b
        bookstore.noofbooks=bookstore.noofbooks+1 

    def display(self):
        print(self.name,"by",self.author,". no of books: ",bookstore.noofbooks)

def main():
    obj1 = bookstore("linux system programming","Robert Love")
    obj1.display()

    obj2 = bookstore("C programming","Dennis Ritchie")
    obj2.display()
    
if __name__ == "__main__":
    main()