import csv

def makeNewCsv(path, itr):
    with open(path + ".csv", "w+") as newCsvWrite:
        csvWrite = csv.writer(newCsvWrite)
        for line in itr:
            csvWrite.writerow(line)
        newCsvWrite.close()