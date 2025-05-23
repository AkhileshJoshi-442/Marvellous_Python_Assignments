def vote(no):
    if (no>=18):
        print("eligible to vote")
    else:
        print("not eligible to vote")


def main():
    print("enter age")
    age=int(input())
    vote(age)

if __name__=="__main__":
    main()