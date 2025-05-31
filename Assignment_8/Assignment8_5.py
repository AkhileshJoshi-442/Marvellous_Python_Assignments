import threading

def increasing():
    print("numbers from 1 to 50: ")
    for i in range(1,51):
        print(i)
    print()

def decreasing():
    print("numbers from 50 to 1: ")
    for i in range(50,0,-1):
        print(i)
    print()

def main():
 
    Thread1 = threading.Thread(target=increasing)
    Thread2 = threading.Thread(target=decreasing)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__=="__main__":
    main()