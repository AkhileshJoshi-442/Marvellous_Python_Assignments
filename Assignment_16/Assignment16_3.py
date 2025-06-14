def countlines(fname):
    fobj=open(fname,"r")
    lines=fobj.readlines()
    print("number of lines: ",len(lines))

def countwords(fname):
    fobj=open(fname,"r")
    data=fobj.read()
    count=len(data.split())
    print("number of words: ",count)

def countchar(fname):
    fobj=open(fname,"r")
    data=fobj.read()
    print("number of characters: ",len(data))

def main():
    print("enter name of file: ")
    filename=input()
    countlines(filename)
    countwords(filename)
    countchar(filename)

if __name__=="__main__":
    main()