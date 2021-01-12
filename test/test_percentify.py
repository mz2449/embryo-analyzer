import unittest
import csv_functions
import pixel_to_embryo_length
import percentify


class TestPercentify(unittest.TestCase):
    def test_percentify(self):
        expected = [[100.0, 0.0], [90.0, 10.0], [80.0, 15.0], [70.0, 50.0], [60.0, 80.0], [50.0, 100.0], [40.0, 80.0],
                    [30.0, 45.0], [20.0, 35.0], [10.0, 15.0], [0.0, 5.0]]
        actual = csv_functions.csv_open('test_1.csv')
        actual = pixel_to_embryo_length.pixel_to_embryo_length(actual)
        percentify.percentify(actual)
        self.assertEqual(expected, actual)

        expected = [[100.0, 0.0], [90.0, 10.0], [80.0, 15.0], [70.0, 50.0], [60.0, 80.0], [50.0, 100.0], [40.0, 80.0],
                    [30.0, 45.0], [20.0, 35.0], [10.0, 15.0], [0.0, 5.0]]
        actual = csv_functions.csv_open('test_2.csv')
        actual = pixel_to_embryo_length.pixel_to_embryo_length(actual)
        percentify.percentify(actual)
        self.assertEqual(expected, actual)
