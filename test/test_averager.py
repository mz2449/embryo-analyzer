import unittest
import csv_functions
import pixel_to_embryo_length
import _averager


class TestAverager(unittest.TestCase):
    def test_averager(self):
        file_list = [pixel_to_embryo_length.pixel_to_embryo_length(csv_functions.csv_open('test_1.csv')),
                     pixel_to_embryo_length.pixel_to_embryo_length(csv_functions.csv_open('test_2.csv'))]
        actual = _averager.averager(file_list)
        expected = [[100.0, 150], [90.0, 135], [80.0, 127.5], [70.0, 75], [60.0, 30], [50.0, 0], [40.0, 30],
                    [30.0, 82.5], [20.0, 97.5], [10.0, 127.5], [0.0, 142.5]]
        self.assertEqual(expected, actual)
