add= lambda A,B : A+B
subtract= lambda A,B : A-B
divide= lambda A,B : A/B
multiply= lambda A,B : A*B


def main():
    print("enter first number: ")
    no1=int(input())
    print("enter first number: ")
    no2=int(input())

    r1=add(no1,no2)
    print("sum: ",r1)
    r2=subtract(no1,no2)
    print("difference: ",r2)
    r3=divide(no1,no2)
    print("division: ",r3)
    r4=multiply(no1,no2)
    print("product: ",r4)


if __name__=="__main__":
    main()