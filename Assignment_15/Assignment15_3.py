import sys   
def main():
    fobj=open(sys.argv[1],"r")
    data=fobj.read()
    fobj1=open("demo.txt","w")
    fobj1.write(data)
    fobj1=open("demo.txt","r")
    data=fobj1.read()
    print("contents of demo.txt: \n",data)

if __name__=="__main__":
    main()