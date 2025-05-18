from functools import reduce

def chkprime (num): 
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return 0
                break
        else:
            return  1
    else:
        return 0
        
mult=lambda A : A*2

max=lambda A,B : A if A>B else B


def main():
    data=[]
    print("enter no of elements")
    size=int(input())

    print("enter numeric values")
    for i in range(size):
        no=int(input())
        data.append(no)

    print("input data",data)

    fdata=list(filter(chkprime,data))
    print("list after filter : ",fdata)

    mdata=list(map(mult,fdata))
    print("list after map : ",mdata)

    rdata=reduce(max,mdata)
    print("ouput of reduce : ",rdata)

if __name__=="__main__":
    main()
