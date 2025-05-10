def ChkNum(no):
    no1=no%2
    if(no1==0):
        print("given number is even")
    else:
        print("given number is odd") 

def Main():
    print("enter any number:")
    num=int(input())
    ChkNum(num)    
    
if __name__=="__main__":
    Main()

