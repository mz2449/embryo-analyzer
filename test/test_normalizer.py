import unittest
import csv_functions
import pixel_to_embryo_length
import normalizer


class TestNormalizer(unittest.TestCase):
    def test_normalizer(self):
        norm_file = csv_functions.csv_open('test_norm.csv')
        expected = [[100.0, 0], [90.0, 5], [80.0, 7.5], [70.0, 25], [60.0, 40], [50.0, 50], [40.0, 40],
                    [30.0, 22.5], [20.0, 17.5], [10.0, 7.5], [0.0, 2.5]]
        actual = csv_functions.csv_open('test_1.csv')
        actual = pixel_to_embryo_length.pixel_to_embryo_length(actual)
        normalizer.normalize(actual, norm_file)
        self.assertEqual(expected, actual)

        expected = [[100.0, 0], [90.0, 4], [80.0, 6], [70.0, 20], [60.0, 32], [50.0, 40],
                    [40.0, 32], [30.0, 18], [20.0, 14], [10.0, 6], [0.0, 2]]
        actual = csv_functions.csv_open('test_2.csv')
        actual = pixel_to_embryo_length.pixel_to_embryo_length(actual)
        normalizer.normalize(actual, norm_file)
        self.assertEqual(expected, actual)
