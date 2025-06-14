def main():
    fobj=open("student.txt","w")
    fobj.write("student a \n")
    fobj.write("student b \n")
    fobj.write("student c \n")
    fobj.write("student d \n")
    fobj.write("student e \n")
    fobj=open("student.txt","r")
    data=fobj.read()
    print("contents of file student.txt :\n",data)

if __name__=="__main__":
    main()