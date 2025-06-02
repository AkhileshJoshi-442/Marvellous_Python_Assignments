from functools import reduce
filt=lambda A : 70<=A<=90

increase=lambda A : A+10

product=lambda A,B : A*B


def main():
    data=[]
    print("enter no of elements")
    size=int(input())

    print("enter numeric values")
    for i in range(size):
        no=int(input())
        data.append(no)

    print("input data",data)

    fdata=list(filter(filt,data))
    print("list after filter : ",fdata)

    mdata=list(map(increase,fdata))
    print("list after map : ",mdata)

    rdata=reduce(product,mdata)
    print("ouput of reduce : ",rdata)

if __name__=="__main__":
    main()