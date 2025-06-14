def main():
    print("enter 10 numbers: ")
    fobj=open("numbers.txt","w")
    for i in range(10):
        value=int(input())
        fobj.writelines(str(value)+"\n")

    fobj=open("numbers.txt","r")
    ret=fobj.read()
    print("contents of file numbers.txt :\n",ret)

if __name__=="__main__":
    main()