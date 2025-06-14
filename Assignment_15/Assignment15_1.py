import os
def check(fname):
    ret=os.path.exists(fname)
    if ret==True:
        print("file is present in current dictionary")
    else:
        print("there is no such file")
    
def main():
    print("enter name of the file: ")
    filename=input()
    check(filename)

if __name__=="__main__":
    main()