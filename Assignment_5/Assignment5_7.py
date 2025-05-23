def area(l,w):
    a=l*w
    print("area of rectangle: ",a)

def parameter(l,w):
    p=2*(l+w)
    print("parameter of rectangle: ",p)


def main():
    print("enter length of a rectangle:")
    length=int(input())
    print("enter width of a rectangle:")
    width=int(input())

    area(length,width)
    parameter(length,width)

if __name__=="__main__":
    main()

