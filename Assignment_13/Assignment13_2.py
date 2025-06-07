class bankaccount:
    roi = 10.5

    def __init__(self):
        self.name = str(input("enter name: "))
        self.amount = float(input("enter amount: "))

    def deposit(self):
        print("amount to deposit: ")
        dep_amount=int(input())
        self.amount=self.amount+dep_amount

    def withdraw(self):
        print("amount to withdraw: ")
        wid_amount=int(input())
        self.amount=self.amount-wid_amount

    def calculateinterest(self):
        interest = (self.amount*bankaccount.roi) /100
        print("interest is: ",interest)

    def display(self):
        print("name: ",self.name)
        print("amount: ",self.amount)
    
def main():
    obj1 = bankaccount()
    obj1.deposit()
    obj1.withdraw()
    obj1.calculateinterest()
    obj1.display()

if __name__ == "__main__":
    main()