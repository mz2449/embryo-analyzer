def percentify(itr):
    newItr = []
    maxNum = float(itr[1][-1])
    minNum = float(itr[1][-1])
    for line in itr:
        if float(line[-1]) > maxNum:
            maxNum = float(line[-1])
        if float(line[-1]) < minNum:
            minNum = float(line[-1])
    maxNum -= minNum

    for line in itr:
        newNum = round((((float(line[-1]) - minNum) / maxNum ) * 100), 2)
        newLine = line
        newLine[-1] = str(newNum)
        newItr.append(newLine)

    return newItr