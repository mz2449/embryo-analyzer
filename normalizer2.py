def removeFirstElement(itr):
    newItr = []
    for line in itr:
        try: #only do this if the rows first element is a number otherwise skip
            if isinstance(int(line[0]), int):
                newItr.append(line)
                continue
        except: #except has no append, therefore any rows where numbers are not in the first element are removed
            continue

    return newItr

def normalize(iter1, norm, meanLabel):
    mean = float(norm[meanLabel])
    for line in iter1:
        line [1] = str((float(line[1]) / mean) / (255/mean)))
