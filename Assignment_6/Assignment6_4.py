def factorial(no):
    val=1
    for i in range(no,0,-1):
        val=val*i
    print("factorial of",no,"is: ",val)

def main():
    print("enter a number: ")
    x=int(input())
    factorial(x)


if __name__=="__main__":
    main()