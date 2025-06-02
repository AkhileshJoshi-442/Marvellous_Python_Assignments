def printnum_iteration(no):
    i=1
    while(i<=no):
        print(i,end= " ")
        i=i+1
    print()

i=1
def printnum_recursion(no):
    global i
    if(i<=no):
        print(i,end= " ")
        i=i+1
        printnum_recursion(no)
        print()

def main():
    print("enter a number:")
    num=int(input())
    printnum_iteration(num)
    printnum_recursion(num)

if __name__=="__main__":
    main()