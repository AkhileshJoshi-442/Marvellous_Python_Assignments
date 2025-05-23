chkeven=lambda A: (A%2==0)

def main():
    print("enter no of elements")
    size=int(input())
    data=[]
    print("enter values")
    for i in range(size):
        no=int(input())
        data.append(no)

    fdata=list(filter(chkeven,data))
    print("even numbers: ",fdata)

if __name__=="__main__":
    main()