def check(fname,word):
    fobj=open(fname,"r")
    data=fobj.read()
    count=0
    sum=data.count(word)

    for i in data:
        if i==word:
            count=count+1
    print("frequency of given string in file: ",sum)

def main():
    print("enter name of the file: ")
    filename=input()
    print("enter string to be searched: ")
    string=input()

    check(filename,string)

if __name__=="__main__":
    main()