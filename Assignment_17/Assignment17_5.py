import schedule
import time

def logtime():
    fobj = open("TIMELog.txt","a")
    timestamp=time.ctime()
    fobj.write(timestamp+"\n")

def main():

    schedule.every(5).minutes.do(logtime)

    print("Application is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()