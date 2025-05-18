
def addition(no):
    length=len(str(no))
    sum=0
    for i in range(length):
        digit=no%10
        sum=sum+digit
        no=no//10
    print(sum)    

def main():
    print("enter number:")
    num=int(input())
    addition(num)


if __name__=="__main__":
    main()