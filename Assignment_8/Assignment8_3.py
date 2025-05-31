import threading

def evenlist(values):
    sum=0
    print("addition of even numbers: ")
    for i in values:
        if (i%2==0):
            sum=sum+i
    print(sum)

def oddlist(values):
    sum=0
    print("addition of odd numbers: ")
    for i in values:
        if (i%2!=0):
            sum=sum+i
    print(sum)

def main():
    print("enter number of elements: ")
    size=int(input())
    data=[]

    print("enter numeric values: ")
    for i in range(size):
        no=int(input())
        data.append(no)
    print("the list is: ",data)
 
    T1 = threading.Thread(target=evenlist , args=(data,))
    T2 = threading.Thread(target=oddlist , args=(data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("exit from main")

if __name__=="__main__":
    main()