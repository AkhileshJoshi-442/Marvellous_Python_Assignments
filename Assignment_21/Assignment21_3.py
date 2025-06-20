import psutil
import os
import time
import sys

def createlog(foldername):
    if not os.path.exists(foldername):
        os.mkdir(foldername)

    timestamp=time.ctime()
    timestamp=timestamp.replace(" ","")
    timestamp=timestamp.replace(":","_")
    timestamp=timestamp.replace("/","_")

    filename=os.path.join(foldername,"marvellous%s.log" %(timestamp))

    fobj=open(filename,"w")

    border="-"*80

    fobj.write(border)
    fobj.write("\n\t\tmarvellous infosystems process log\n")
    fobj.write("\t\tlog file is created at: "+time.ctime()+"\n")
    fobj.write(border)

    data=processscan()
    for value in data:
        fobj.write("%s \n" %value)

    fobj.write(border)

    fobj.close()


def processscan():

    listprocess=[]

    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=["name","pid","username"])
            listprocess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
    dirname=sys.argv[1]
    createlog(dirname)

if __name__=="__main__":
    main()