def pattern1(no):
    for i in range(no,0,-1): 
        for j in range(i): 
            print("*",end=" ")
        print()
        
def main():
    print("enter number:")
    num=int(input())

    pattern1(num)

if __name__=="__main__":
    main()