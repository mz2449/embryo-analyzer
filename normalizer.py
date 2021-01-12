mean_label = 0


def find_mean_label(file_norm):  # arg comes from read normalizing csv, each list is a line in the csv file
    global mean_label
    for line in file_norm:
        for label in line:
            if label.lower() == 'mean':
                mean_label = line.index(label)
        file_norm.remove(line)  # removes this first label line so that the index of the element matches the file number
        break  # acts only on the first line in the .csv, which should house the labels, eg: '[' ', 'Label', 'Mean']'


def normalize(list_file, list_norm):
    find_mean_label(list_norm)
    mean = float(list_norm[0][mean_label])
    for line in list_file:
        line[-1] = line[-1] / mean
    list_norm = list_norm[1:]
