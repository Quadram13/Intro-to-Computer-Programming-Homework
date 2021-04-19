"""
Marcus Du
4/15/2021
Section 006
Part 1
"""
inputlist = [10, 20, 30, 40, 50]

def listlen(inputlist):
    counter=0
    for i in inputlist:
        counter+=1
    return counter
    

def listmax(inputlist):
    max = inputlist[0]
    for i in range(0,listlen(inputlist)):
        if inputlist[i] >= max:
            max = inputlist[i]
    return max

def listcopy(inputlist):
    newlist=inputlist
    return newlist

def listappend(inputlist,newelement):
    Lcopy=[]
    Lcopy+=inputlist
    Lcopy+=[newelement]
    return Lcopy

def listinsert(inputlist,index,newelement):
    outputlist=[]
    outputlist=inputlist[0:index]+[newelement]+inputlist[index:listlen(inputlist)]
    return outputlist


def listremove(inputlist,element):
    listinstance=[]
    
    for i in range (0,listlen(inputlist)):
        listpart=inputlist[i]
        if element==listpart:
            listinstance+=[i]
    finallist=inputlist[0:listinstance[0]]
    choppedlist=[]
    for j in range(1,listlen(listinstance)):
        choppedlist+=inputlist[(listinstance[j-1]+1):listinstance[j]]
    choppedlist+=inputlist[int(listinstance[listlen(listinstance)-1]+1):int(listlen(inputlist))]
    return listinsert(finallist,1,choppedlist)
    
    


"""
def listreverse(inputlist):
    s = listlen(inputlist)

    outputlist = []
    try:
        for item in inputlist:
            s = s - 1
            outputlist[s] = item
    
    except:
        return outputlist
    

    else:
        break
        
    """

def listreverse(inputlist):
    length = len(inputlist)
    s = length

    new_list = [None]*length

    for item in inputlist:
        s = s - 1
        new_list[s] = item
    return new_list


print(listreverse(inputlist))
    
