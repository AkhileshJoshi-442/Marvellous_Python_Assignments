min= lambda A,B: A<B

def minimum(task , values):
    result=values[0]
    for no in values:
        if(no<result):
            result=no

    print("minimum number from list is:",result)  
    

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()

    print("Enter the values")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("list is :",data)

    minimum(min,data)


if __name__=="__main__":
    main()