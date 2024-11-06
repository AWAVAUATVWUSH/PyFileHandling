import random

def make_list():
    mylist:list = []
    i:int = 0
    while (i<100):
        mylist.append(int(random.random()*201-50))
        i+=1
    return mylist

def list_to_str(mylist:list = []):
    stringToRet:str = ""
    i:int = 0
    iMax:int = len(mylist)
    while (i<iMax-1):
        stringToRet += f"{mylist[i]}; "
        i+=1
    stringToRet += f"{mylist[i]}"
    return stringToRet

def print_to_file(text:str=""):
    fileptr = open("adatok.txt", "w", encoding='utf-8')
    fileptr.write(text)
    fileptr.close()

def read_from_file():
    fileptr = open("adatok.txt", "r", encoding='utf-8')
    fileContentsText:str = fileptr.read()
    fileContentsList:list = fileContentsText.split("; ")
    fileptr.close()
    i:int = 0
    iMax = len(fileContentsList)
    while(i<iMax):
        fileContentsList[i] = int(fileContentsList[i].strip())
        i+=1
    return fileContentsList