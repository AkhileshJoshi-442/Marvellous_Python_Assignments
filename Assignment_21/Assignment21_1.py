import psutil

def processdisplay():
    border="*"*80
    print(border)
    print("information of currently running processes : ")
    print(border)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            print(info)
        except Exception:
            print("Exception occured")

def main():
    processdisplay()

if __name__=="__main__":
    main()