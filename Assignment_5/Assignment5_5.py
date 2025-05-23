def evenodd(no):
    if (no%2==0):
        print(no,"is an even number")
    else:
        print(no,"is an odd number")

def main():
    print("enter a number")
    num=int(input())
    evenodd(num)

if __name__=="__main__":
    main()