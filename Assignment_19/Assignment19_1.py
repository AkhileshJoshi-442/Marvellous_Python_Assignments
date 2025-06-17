import os
import sys

def directorywatcher(directoryName,ext):

    fobj=open("ass19q1","a")

    flag = os.path.isabs(directoryName)

    if(flag == False):
        directoryName = os.path.abspath(directoryName)

    flag = os.path.exists(directoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(directoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
    
    fobj.write("files with extension "+ext+" are :\n")
    for FolderName , SubFolderNames, FileNames in os.walk(directoryName):
        for fname in FileNames:
            if fname.endswith(ext):
                fobj.write(fname+"\n")

def main():
    dirName = sys.argv[1]
    extension= sys.argv[2]

    directorywatcher(dirName,extension)

if __name__ == "__main__":
    main()