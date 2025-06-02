from functools import reduce
checkeven=lambda A:(A%2==0)

square=lambda A : A**2

add=lambda A,B : A+B


def main():
    data=[]
    print("enter no of elements")
    size=int(input())

    print("enter numeric values")
    for i in range(size):
        no=int(input())
        data.append(no)

    print("input data",data)

    fdata=list(filter(checkeven,data))
    print("list after filter : ",fdata)

    mdata=list(map(square,fdata))
    print("list after map : ",mdata)

    rdata=reduce(add,mdata)
    print("ouput of reduce : ",rdata)

if __name__=="__main__":
    main()