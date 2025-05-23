
def chkprime(no):
    factor=1
    for i in range(1,no+1):
        if no%i==0:
            factor=factor*i
    if factor==no:
        return 1
    else:
        return 0

def main():
    print("enter no of elements")
    size=int(input())
    data=[]
    print("enter values")
    for i in range(size):
        no=int(input())
        data.append(no)

    fdata=list(filter(chkprime,data))
    print("prime numbers: ",fdata)

if __name__=="__main__":
    main()