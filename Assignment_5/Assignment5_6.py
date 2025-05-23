def fahrenheit(value):
    result=(value*9/5)+32
    print("temperature in fahrenheit: ",result)

def main():
    print("enter temperature in celsius: ")
    celsius=float(input())
    fahrenheit(celsius)

if __name__=="__main__":
    main()