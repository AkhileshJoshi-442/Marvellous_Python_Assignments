import threading

def even():
    print("even numbers: ")
    for i in range(2,21,2):
        print(i)

def odd():
    print("odd numbers: ")
    for i in range(1,20,2):
        print(i)

def main():
 
    T1 = threading.Thread(target=even)
    T2 = threading.Thread(target=odd)

    T1.start()
    T1.join()
    
    T2.start()
    T2.join()

if __name__=="__main__":
    main()