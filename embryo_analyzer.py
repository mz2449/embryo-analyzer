import averager
import normalizer
import csv_functions
import pixel_to_embryo_length as pixel
import percentify
import time
import sys
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def fit_gaussian():
    p_file = [['', 'Stripe 2', 'Stripe 3', 'Stripe 7']]
    files = input('files?')

    left_window_23 = float(input('stripe23 left window'))
    right_window_23 = float(input('stripe23 right window'))

    left_window_7 = float(input('stripe7 left window'))
    right_window_7 = float(input('stripe7 right window'))

    norm_list = input('normalizing values (keep in order)').split()

    list_of_files = files.split()
    file_count = 0

    while True:
        file_list = list()
        file_path = ''

        # user input section
        while True:  # file paths loop
            try:
                file_path = list_of_files[file_count]
                file_list.append(csv_functions.csv_open(file_path))
                break
            except FileNotFoundError:
                if file_path != 'stop':
                    print('\nFile not found, recheck name or path')
                continue
            except IndexError:
                if file_count > len(file_list):
                    sys.exit('All done :)')
                print('uh oh')
            finally:
                if file_path.lower() == 'restart':
                    print('restarting... \n\n\n')
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

        norm_value = float(norm_list[file_count])

        # analysis section
        start_time = time.process_time()
        ret_list = list()

        for file in file_list:  # normalization
            ret_file = pixel.pixel_to_embryo_length(file)

            normalizer.normalize(ret_file, [['Mean'], [norm_value]])

            ret_list.append(ret_file)

        ret_list = averager.averager(ret_list)

        x = [line[0] for line in ret_list]
        y = [line[1] for line in ret_list]

        left_window7 = x.index(left_window_7)
        right_window7 = x.index(right_window_7) + 1

        left_window23 = x.index(left_window_23)
        right_window23 = x.index(right_window_23) + 1

        x7 = x[left_window7:right_window7]
        y7 = y[left_window7:right_window7]

        x23 = x[left_window23:right_window23]
        y23 = y[left_window23:right_window23]

        # finding stdev of peaks 2 and 3
        stdev_list = ret_list[x.index(60):x.index(50)]
        xcor_ymin = min(stdev_list, key=lambda value: value[1])[0]
        stdev2 = np.std(y[left_window23:x.index(xcor_ymin)])
        stdev3 = np.std(y[x.index(xcor_ymin):right_window23])

        plt.figure(1, figsize=(10, 7.5))
        plt.xlabel('Embryo Length')
        plt.ylabel('Normalized Intensity')
        plt.title('Fit of Stripe 7')
        plt.axis([100, 0, 0, 2])
        plt.scatter(x, y, color='k', label='data', marker='.', s=1)

        p7, p7_cov = curve_fit(gauss_7, x7, y7, p0=[0.981, 21.8, np.std(y7)])
        p23, p23_cov = curve_fit(gauss_23, x23, y23, p0=[1.174, 60.9, stdev2, 0, 50.7, stdev3])

        # noinspection PyTypeChecker.973
        plt.plot(x[right_window23:x.index(0)], gauss_7(x[right_window23:x.index(0)], *p7), color='r',
                 label='fit for 7th stripe')
        plt.plot(x[0: left_window7], gauss_23(x[0:left_window7], *p23), color='r', label='fit for 2nd and 3rd stripe')

        plt.legend(loc='best')

        plt.savefig(file_path.strip('.csv') + '.png', dpi=600)

        plt.clf()

        p_file.append(['a', p23[0], p23[3], p7[0], file_path.split('/')[-1]])
        p_file.append(['x0', p23[1], p23[4], p7[1]])
        p_file.append(['sigma', p23[2], p23[5], p7[2]])
        p_file.append(['', '', '', ''])

        csv_functions.make_new_csv('/'.join(file_path.split('/')[:-1]) + '/' +
                                   file_path.split('/')[-1].split('_')[0] + 'params', p_file)

        file_count += 1

        stop_time = time.process_time()

        print('\n' + file_path.strip('.csv'))
        print('Finished in', round((stop_time - start_time), 5), 'seconds!')


def gauss_7(x, a, x0, sigma):
    return a * np.exp(- (x - x0) ** 2 / (2 * sigma ** 2))


def gauss_23(x, a_1, x0_1, sigma_1, a_2, x0_2, sigma_2):
    return a_1 * np.exp(- (x - x0_1) ** 2 / (2 * sigma_1 ** 2)) + \
           a_2 * np.exp(- (x - x0_2) ** 2 / (2 * sigma_2 ** 2))


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
                if file_path == 'gaussian':
                    break
                if file_path.lower() == 'restart':
                    print('restarting... \n\n\n')
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                if file_path == '':
                    print('All Files Selected')
                    break

        if file_path == 'gaussian':
            fit_gaussian()
            continue

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

        ret_list = averager.averager(ret_list)

        # ret_list[0] += stdev

        stop_time = time.process_time()

        print('\nFinished in', round((stop_time - start_time), 5), 'seconds!')

        if len(file_list) == 0:
            print('\nIf you didn\'t want to do anything, why did you run me?')
            sys.exit()

        plt.plot([line[0] for line in ret_list], [line[1] for line in ret_list])
        plt.axis([100, 0, 0, 1.5])
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
    fit_gaussian()
    # main()
