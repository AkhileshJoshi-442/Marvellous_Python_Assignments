def chkprime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
            

def main():
    print("enter number:")
    no=int(input())
    chkprime(no)

if __name__=="__main__":
    main()
    