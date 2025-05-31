import threading 

def main():
    string=str(input("Enter string: "))
    small=threading.Thread(target=lowerCase,args=(string,))
    capital=threading.Thread(target=uppercase,args=(string,))
    digits=threading.Thread(target=digit,args=(string,))


    small.start()
    small.join()
    
    capital.start()
    capital.join()

    digits.start()
    digits.join()

    print("end of main")
                           
if __name__=="__main__":
    main() 