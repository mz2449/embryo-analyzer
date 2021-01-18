import averager
import normalizer
import csv_functions
import pixel_to_embryo_length as pixel
import percentify
import time
import sys
import os
import matplotlib.pyplot as plt


def main():
    while True:  # main loop
        file_list = list()
        file_path = ''

        # user input section
        while True:  # file paths loop
            try:
                while True:  # asking for file paths loop
                    file_path = input(f'\nEnter path to File {len(file_list) + 1}' +
                                      '\n(Press Enter when done or \'restart\' to restart):')
                    file_list.append(csv_functions.csv_open(file_path))
            except FileNotFoundError:
                if file_path != '' and file_path.lower() != 'restart':
                    print('\nFile not found, recheck name or path')
            finally:
                if file_path.lower() == 'restart':
                    print('restarting... \n\n\n')
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                if file_path == '':
                    print('All Files Selected')
                    break

        while True:  # asking for normalization loop
            answer_norm = input('\nWould you like to normalize your file? (y/n)')
            if answer_norm in ('y', 'n'):
                break
            else:
                print('\nPlease enter either \'y\' (yes) or \'n\' (no)')
                continue

        file_norm = ''

        if answer_norm == 'y':  # opening normalizing file
            while True:  # asking for normalizing file path loop
                file_norm = input('\nName or Path of File to Normalize to?')
                try:
                    file_norm = csv_functions.csv_open(
                        file_norm)  # file_norm is a list of every line in the file (also a list) (a list of lists)
                    break
                except FileNotFoundError:
                    print('\nFile not found, recheck name or path')
                    continue

        while True:  # asking for percentify loop
            answer_percentify = input("\nWould you like to percentify your file? (y/n)")
            if answer_percentify in ('y', 'n'):
                break
            else:
                print('\nPlease enter either \'y\' (yes) or \'n\' (no)')
                continue

        # analysis section
        start_time = time.process_time()
        ret_list = list()

        for file in file_list:  # normalization and percentification
            ret_file = pixel.pixel_to_embryo_length(file)
            if answer_norm == 'y':
                normalizer.normalize(ret_file, file_norm)
            if answer_percentify == 'y':
                percentify.percentify(ret_file)

            ret_list.append(ret_file)

        stdev = stats.st_dev(ret_list)

        ret_list = averager.averager(ret_list)

        # ret_list[0] += stdev

        stop_time = time.process_time()

        print('\nFinished in', round((stop_time - start_time), 5), 'seconds!')

        if len(file_list) == 0:
            print('\nIf you didn\'t want to do anything, why did you run me?')
            sys.exit()

        plt.plot([line[0] for line in ret_list], [line[1] for line in ret_list])
        plt.axis([0, 100, 0, 1.5])
        plt.show()

        # final section
        new_name = input('New .csv file name?')
        while True:
            new_path = input('\nPath to new .csv file?')
            try:
                if new_name[-1] == "/":
                    csv_functions.make_new_csv(new_path + new_name, ret_list)
                else:
                    csv_functions.make_new_csv(new_path + "/" + new_name, ret_list)
                print(f'File {new_name} created at {new_path}')
                break
            except:
                print('Error creating new .csv, try different path')

        while True:  # asking to continue loop
            answer_continue = input('\nDo you have more to analyze (y/n): ')
            if answer_continue in ('y', 'n'):
                break
            else:
                print('\nPlease enter either y (yes) or n (no)')
                continue

        if answer_continue == 'n':
            print('\nGoodbye')
            sys.exit()


if __name__ == '__main__':
    main()
