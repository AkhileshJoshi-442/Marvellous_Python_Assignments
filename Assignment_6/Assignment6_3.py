def table(no):
    x=0
    for i in range(1,11):
        x=no*i
        print(no,"x",i,"=",x)

def main():
    print("enter a number")
    num=int(input())
    table(num)


if __name__=="__main__":
    main()