max= lambda A,B : A>B

def maximum(task,values):
    result=values[0]
    for no in values:
        if(no>result):
            result=no

    print("maximum number from list is:",result)  

def main():
    print("enter 5 numbers")
    data=[]
    for i in range(5):
        no=int(input())
        data.append(no)
    maximum(max,data)

if __name__=="__main__":
    main()