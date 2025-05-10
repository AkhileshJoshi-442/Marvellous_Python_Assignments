def count(name):
    result=len(name)
    return result

def Main():
    print("enter your name:")
    n=input()
    output=count(n)
    print("length of the name is:",output)

if __name__=="__main__":
    Main()



