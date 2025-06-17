import sys
def main():
    fobj1=open(sys.argv[1],"r")
    data1=fobj1.read()
    fobj2=open(sys.argv[2],"r")
    data2=fobj2.read()
    if data1==data2:
        print("Result: success")
    else:
        print("Result: failure")

if __name__=="__main__":
    main()