max= lambda A,B: A>B

def maximum(task , values):
    result=values[0]
    for no in values:
        if(no>result):
            result=no

    print("maximum number from list is:",result)  
    

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()

    print("Enter the values")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("list is :",data)

    maximum(max,data)


if __name__=="__main__":
    main()

