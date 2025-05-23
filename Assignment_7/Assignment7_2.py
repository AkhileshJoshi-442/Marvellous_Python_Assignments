double=lambda A: A*2

def main():
    print("enter no of elements")
    size=int(input())
    data=[]
    print("enter values")
    for i in range(size):
        no=int(input())
        data.append(no)

    mdata=list(map(double,data))
    print("doubled list: ",mdata)

if __name__=="__main__":
    main()