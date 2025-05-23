from functools import reduce

product=lambda A,B: A*B

def main():
    print("enter no of elements")
    size=int(input())
    data=[]
    print("enter values")
    for i in range(size):
        no=int(input())
        data.append(no)

    rdata=reduce(product,data)
    print("even numbers: ",rdata)

if __name__=="__main__":
    main()