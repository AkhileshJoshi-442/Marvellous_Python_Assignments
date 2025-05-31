import multiprocessing.process
import time
import threading
import multiprocessing

def add():
    sum=0
    for i in range(10000001):
        sum=sum+i
    print("sum of numbers from 1 to 10 million: ",sum)

def main():

    normal_start=time.time()
    print("execution by normal function: ")
    add()
    normal_end=time.time()
    print("time required for normal fuction:",normal_end-normal_start)
    print()


    threading_start=time.time()
    print("execution by threading: ")
    T1 = threading.Thread(target=add)
    T1.start()
    T1.join()
    threading_end=time.time()
    print("time required for threading:",threading_end-threading_start)
    print()


    multiprocessing_start=time.time()
    print("execution by multiprocessing: ")
    P1 = multiprocessing.Process(target=add)
    P1.start()
    P1.join()
    multiprocessing_end=time.time()
    print("time required for multiprocessing:",threading_end-threading_start)
    print()


if __name__=="__main__":
    main()