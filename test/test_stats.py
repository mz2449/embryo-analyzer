import csv_functions
import pixel_to_embryo_length
import stats
import unittest


class TestStats(unittest.TestCase):
    def test_stdev(self):
        file1 = csv_functions.csv_open('test_1.csv')
        file2 = csv_functions.csv_open('test_2.csv')

        file_list = [pixel_to_embryo_length.pixel_to_embryo_length(file1),
                     pixel_to_embryo_length.pixel_to_embryo_length(file2)]

        expected = 56.994056802640

        actual = round(stats.st_dev(file_list)[2], 12)

        self.assertEqual(expected, actual)
