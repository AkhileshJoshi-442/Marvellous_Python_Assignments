square=lambda A: A**2
cube=lambda A: A**3

def main():
    print("enter a number")
    num=int(input())
    print("square:",square(num))
    print("cube:",cube(num))

if __name__=="__main__":
    main()


