import threading
import time

def fun():
    print("Numbers: ")
    for i in range(1,6):
        print(i)

def main():
 
    T1 = threading.Thread(target=fun)
    T2 = threading.Thread(target=fun)
    T3 = threading.Thread(target=fun)

    T1.start()
    T1.join()

    time.sleep(1)

    T2.start()
    T2.join()

    time.sleep(1)

    T3.start()
    T3.join()

if __name__=="__main__":
    main()