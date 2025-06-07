class book:
    def __init__(self,a):
        self.__price = a

    def get(self):
        return self.__price

    def set(self):
        newprice=int(input("enter new price:"))
        self.__price = newprice

    def display(self):
        print("Book Price: ",self.__price)

def main():
    
    book1=book(400)
    book1.get()
    book1.display()
    book1.set()
    book1.display()          
    
if __name__ == "__main__":
    main()