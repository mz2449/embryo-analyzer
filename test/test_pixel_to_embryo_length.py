import unittest
import csv_functions
import pixel_to_embryo_length


class TestPixelToEmbryoLength(unittest.TestCase):
    def test_open_test_file(self):
        expected = [[100.0, 0], [90.0, 10], [80.0, 15], [70.0, 50], [60.0, 80], [50.0, 100], [40.0, 80],
                    [30.0, 45], [20.0, 35], [10.0, 15], [0.0, 5]]
        actual = pixel_to_embryo_length.pixel_to_embryo_length(csv_functions.csv_open('test_1.csv'))
        self.assertEqual(expected, actual)

        expected = [[100.0, 0], [90.0, 20], [80.0, 30], [70.0, 100], [60.0, 160], [50.0, 200],
                    [40.0, 160], [30.0, 90], [20.0, 70], [10.0, 30], [0.0, 10]]
        actual = pixel_to_embryo_length.pixel_to_embryo_length(csv_functions.csv_open('test_2.csv'))
        self.assertEqual(expected, actual)
