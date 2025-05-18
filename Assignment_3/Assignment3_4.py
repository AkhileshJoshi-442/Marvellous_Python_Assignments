freq= lambda A,B: A==B

def frequency(task , values,num):
    result=0
    for no in values:
        if(no==num):
            result=result+1

    print(" given number repeated :",result)  
    

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()

    print("Enter the values")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("list is :",data)

    print("enter number to be searched:")
    number=int(input())

    frequency(freq,data,number)


if __name__=="__main__":
    main()