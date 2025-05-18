import Arithmetic

def main():
    print("enter first number:")
    num1=int(input())
    print("enter second number:")
    num2=int(input())

    resultadd=Arithmetic.add(num1,num2)
    print("addition is :",resultadd)

    resultsub=Arithmetic.sub(num1,num2)
    print("subtraction is :",resultsub)

    resultmult=Arithmetic.mult(num1,num2)
    print("multiplication is :",resultmult)
    
    resultdiv=Arithmetic.div(num1,num2)
    print("division is :",resultdiv)
    

if __name__=="__main__":
    main()
