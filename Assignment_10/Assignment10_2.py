product=lambda A,B: A*B

def main():
    print("enter two numbers")
    no1=int(input())
    no2=int(input())
    
    ret=product(no1,no2)
    print("product: ",ret)

if __name__=="__main__":
    main()