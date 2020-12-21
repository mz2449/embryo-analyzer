def compiler1(args): #takes in argument that is a list of lists and shoves them all together, returns that list shoved together
    listArgs = list()
    for element in list(args):
        for secondElement in element:
            listArgs.append(secondElement)
    return listArgs

def compiler2(itr): #takes any list and returns a dictionary where same key have values placed together
    newDict = dict()
    for line in itr:
        if line[0] not in newDict.keys():
            newDict.update( {line[0] : [float(line[1])]} )
        elif line[0] in newDict.keys():
            newDict[line[0]] += [float(line[1])]
    return newDict

def compiler(*args):
    c1Result = compiler1(*args)
    ret = compiler2(c1Result)
    return ret

def averager(d): #takes in dict and averages out all values in the dict
    for key in d:
        s = 0

        for n in d[key]:
            s += n

        average = s / len(d[key])
        d[key] = str(average)

def deDictionaryer(d): #takes dictionary and returns list with subsets of list as keys, values
    newList = list()
    for key, value in d.items(): #ligma
        tempElement = [key, value]
        newList.append(tempElement)
    return newList


def sorter(itr):
    newItr = sorted(itr, key=lambda byPercentage: float(byPercentage[0]), reverse=True) #sort by percentage which is the first element
    return newItr