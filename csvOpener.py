import csv

def csvOpener(path):
    with open(path) as csvRFile:
        csvRead = csv.reader(csvRFile)
        csvFile = []
        for line in csvRead:
            csvFile.append(line)
        csvRFile.close()
    return csvFile
