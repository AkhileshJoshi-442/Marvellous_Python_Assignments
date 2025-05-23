def largest(n1,n2,n3):
    if (n1>n2):
        if (n1>n3):
            print("largest number is: ",n1)
        else:
            print("largest number is: ",n3)
    elif (n2>n3):
        print("largest number is: ",n2)
    else:
        print("largest number is: ",n3)

def main():
    print("enter three numbers")
    no1=int(input())
    no2=int(input())
    no3=int(input())
    largest(no1,no2,no3)

if __name__=="__main__":
    main()
