import os
import sys
import hashlib

def calculatechecksum(path, BlockSize = 1024):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def directorywatcher(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = calculatechecksum(fname)
            print("File name : ",fname)
            print("Checksum : ",checksum)
            print()

def main():

    directorywatcher(sys.argv[1])
    
if __name__ == "__main__":
    main()