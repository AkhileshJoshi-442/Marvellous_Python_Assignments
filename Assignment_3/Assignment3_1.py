add= lambda A,B: A+B

def addition(task , Values):
    result = 0
    for no in Values:
        result = result + no

    print("addition of elements is:",result)    
    

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()

    print("Enter the values")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("list is :",data)

    addition(add,data)


if __name__=="__main__":
    main()

