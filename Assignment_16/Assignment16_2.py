def main():
    fobj=open("data.txt","r")
    data=fobj.read()
    print("contents of file data.txt :\n",data)

if __name__=="__main__":
    main()