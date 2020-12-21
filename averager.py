def compiler1(args): #takes in argument that is a list of lists and shoves them all together, returns that list shoved together
    listArgs = list()
    for element in args:
        for secondElement in element:
            listArgs.append(secondElement)
    return listArgs

def compiler2(itr): #takes any list and returns a dictionary where same key has values placed together
    newDict = dict()
    for line in itr:
        if line[0] not in newDict.keys():
            newDict.update( {line[0] : [float(line[1])]} )
        elif line[0] in newDict.keys():
            newDict[line[0]] += [float(line[1])]
    return newDict

def compiler(*args): #puts compiler 1 and 2 together
    return compiler2(compiler1(*args))

def bringToZero(itr): #takes a dictionary and subtracts every value by the highest plot value to bring the baseline to zero
    minNum = max(list(itr.values())) #imageJ values range from 0 - 255 with 0 being the DARKEST and 255 the LIGHTEST
    for key, value in itr.items():
        itr[key] = str(float(minNum) - float(itr[key]))

def averager(d): #takes in dict and averages out all values in the dict
    for key in d:
        sum = 0

        for value in d[key]:
            sum += value

        average = sum / len(d[key])
        d[key] = float(average)
    bringToZero(d)

def deDictionaryer(d): #takes dictionary and returns list with subsets of list as keys, values
    newList = list()
    for key, value in d.items():
        tempElement = [key, value]
        newList.append(tempElement)
    return newList



def sorter(itr):
    newItr = sorted(itr, key=lambda byPercentage: float(byPercentage[0]), reverse=True) #sort by percentage which is the first element
    return newItr

