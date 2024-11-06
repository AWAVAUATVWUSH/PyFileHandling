def num_of_negatives(inlist:list = []):
    i:int = 0
    iMax = len(inlist)
    numToRet:int = 0
    while(i<iMax):
        if(inlist[i]<0):
            numToRet += 1
        i+=1
    return numToRet

def largest_in_list(inlist:list = []):
    i:int = 0
    iMax = len(inlist)
    numToRet:int = 0
    while(i<iMax):
        if(inlist[i]>numToRet):
            numToRet += inlist[i]
        i+=1
    return numToRet

def get_even_numbers_as_list(inlist:list = []):
    i:int = 0
    iMax = len(inlist)
    listToRet:list = []
    while(i<iMax):
        if(inlist[i]%2==0):
            listToRet.append(inlist[i])
        i+=1
    return listToRet

def sum_of_nums_devisible_by_five(inlist:list = []):
    i:int = 0
    iMax = len(inlist)
    numToRet:int = 0
    while(i<iMax):
        if(inlist[i]%5==0):
            numToRet += inlist[i]
        i+=1
    return numToRet

def index_of_smallest_num(inlist:list = []):
    i:int = 0
    iMax = len(inlist)-1
    numToRet:int = 0
    while(i<iMax):
        if(inlist[i+1]<inlist[numToRet]):
            numToRet = i
        i+=1
    return numToRet