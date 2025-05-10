def check(no):
    if(no==0):
        print("zero")
    elif(no>0):
        print("Positive number")
    else:
        print("Negative number")

def Main():
    print("enter any number")
    num=int(input())
    check(num)

if __name__=="__main__":
    Main()
    