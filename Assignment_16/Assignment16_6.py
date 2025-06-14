def main():
    print("enter name of file to be copied: ")
    file1=input()
    print("enter name of destination file : ")
    file2=input()

    fobj1=open(file1,"r")
    data1=fobj1.read()

    fobj2=open(file2,"w")
    fobj2.write(data1)

    fobj2=open(file2,"r")
    data2=fobj2.read()
    
    print("contents copied in",file2,"from",file1," :\n",data2)

if __name__=="__main__":
    main()