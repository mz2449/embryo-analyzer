import csv

def csv_open(path): #opens .csv file and returns a list with each line as a line in the .csv file
    path = path.strip('\'"') #remove formatting from input
    with open(path) as csv_file:
        csv_read = csv.reader(csv_file)
        csv_file = [line for line in csv_read]
    return csv_file


def make_new_csv(path, itr): #create a new .csv file out of an iterable, and a path
    with open(path + '.csv', 'w', newline='') as new_csv:
        csv_write = csv.writer(new_csv)
        for line in itr:
            csv_write.writerow(line)
