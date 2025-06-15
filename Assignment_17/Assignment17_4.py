import schedule
import time

def display():
    print("Namaskar...\U0001F64F")

def main():

    schedule.every().day.at("09:00").do(display)

    print("Application is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()