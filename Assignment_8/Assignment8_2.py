import threading

def evenfactor(no):
    sum=0
    print("addition of even factors: ")
    for i in range(2,no+1,2):
        if (no%i==0):
            sum=sum+i
    print(sum)

def oddfactor(no):
    sum=0
    print("addition of odd factors: ")
    for i in range(1,no+1,2):
        if (no%i==0):
            sum=sum+i
    print(sum)

def main():
    print("enter a number: ")
    num=int(input())
 
    T1 = threading.Thread(target=evenfactor , args=(num,))
    T2 = threading.Thread(target=oddfactor , args=(num,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("exit from main")

if __name__=="__main__":
    main()