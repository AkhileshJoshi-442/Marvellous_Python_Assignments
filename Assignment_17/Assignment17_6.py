import schedule
import time
import datetime

def lunchtime():
    print("lunch time : ")

def wrapuptime():
    print("wrap up time : ")

def main():

    schedule.every().day.at("13:00").do(lunchtime)

    schedule.every().day.at("18:00").do(wrapuptime)

    print("Application is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()