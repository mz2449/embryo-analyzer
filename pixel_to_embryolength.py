def changeFirstElement(itr):
    newItr = []
    lastElement = itr[-1]
    for line in itr:
        try:
            if isinstance(float(line[0]), float):#only do this if the rows first element is a number otherwise skip
                num = float(line[0])
                newNum = round(float(((float(lastElement[0]) - num) / float(lastElement[0])) * 100), 1)
                """
                IMPORTANT: IMAGEJ PLOTS X CORD START AT 0(ZERO)
                Divide difference between maximum number (lastElement[0]) and original number by maximum number, then
                multiply by 100 to obtain a percentage with 100% at the beginning (equivalent to the original 0)
                (in Drosophila, 100 indicates the anterior)
                """
                newLine = line
                newLine[0] = float(newNum)
                newItr.append(newLine)
                continue
        except: #except has no append, therefore any rows where numbers are not in the first element are removed
            continue

    return newItr