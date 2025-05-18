import MarvellousNum 

def listprime(values):
    prime=[]
    for no in values:
        local=(MarvellousNum.chkprime(no))
        if (local==1):
            prime.append(no)

    result=0
    for i in prime:
        result=result+i
    print("addition is:",result,prime)


def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()

    print("Enter the values")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("list is :",data)

    listprime(data)


if __name__=="__main__":
    main()

