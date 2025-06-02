def factorial_iteration(no):
    fact=1
    while(no>=1):
        fact=fact*no
        no=no-1
    return fact
    
fact=1
def factorial_recursion(no):
    global fact
    if(no>=1):
        fact=fact*no
        no=no-1
        factorial_recursion(no)
    return fact
        
def main():
    print("enter a number:")
    num=int(input())
    result1=factorial_iteration(num)
    print("factorial by iteration: ",result1)
    result2=factorial_recursion(num)
    print("factorial by recursion: ",result2)

if __name__ == "__main__":
    main()