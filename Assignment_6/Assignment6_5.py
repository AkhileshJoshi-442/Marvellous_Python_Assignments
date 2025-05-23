def prime(no):
    factor=1
    for i in range(1,no+1):
        if no%i==0:
            factor=factor*i
    if factor==no:
        print(no,"is a prime number")
    else:
        print(no,"is a not prime number")
        

def main():
    print("enter a number: ")
    num=int(input())
    prime(num)

if __name__=="__main__":
    main()