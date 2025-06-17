import os
def read(fname):
    ret=os.path.exists(fname)
    if ret==True:
        fobj=open(fname,"r")
        data=fobj.read()
        print("file contents: \n",data)
    else:
        print("there is no such file")
    
def main():
    print("enter name of the file: ")
    filename=input()
    read(filename)

if __name__=="__main__":
    main()