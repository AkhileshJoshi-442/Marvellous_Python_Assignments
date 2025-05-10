def asterik(num):
    for num in range(num,0,-1):
        print("*",end=" ")
    

def Main():
    print("enter any number:")
    no=int(input())
    asterik(no)

if __name__=="__main__":
    Main()
