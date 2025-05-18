power=lambda no : 2**no

def main():
    print("enter number:")
    num=int(input())
    result=power(num)
    print("output:",result)

if __name__=="__main__":
    main()

