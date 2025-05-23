def trianglepattern(no):
    for i in range(no+1):
        for j in range(i):
            print("*",end=" ")
        print()

def main():
    print("enter a number")
    num=int(input())
    trianglepattern(num)


if __name__=="__main__":
    main()
