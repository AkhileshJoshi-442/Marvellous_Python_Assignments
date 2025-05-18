def factorsadd(no):
    result=0
    for i in range(1,no):
        if (no%i==0):
            result=result+i
    print("addition of factors is:",result)

def main():
    print("enter a number:")
    num=int(input())

    factorsadd(num)


if __name__=="__main__":
    main()