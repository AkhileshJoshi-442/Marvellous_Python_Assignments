power=lambda A : 2**A

def main():
    print("enter an exponent: ")
    expo=int(input())
    ret=power(expo)
    print("result: ",ret)

if __name__=="__main__":
    main()