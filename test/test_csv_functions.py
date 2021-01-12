import unittest
import csv_functions


class TestCsvFunctions(unittest.TestCase):
    def test_open_test_file(self):
        expected = [['ï»¿X', 'Y'], ['0', '0'], ['1', '10'], ['2', '15'], ['3', '50'], ['4', '80'], ['5', '100'],
                    ['6', '80'], ['7', '45'], ['8', '35'], ['9', '15'], ['10', '5']]
        actual = csv_functions.csv_open('test_1.csv')
        self.assertEqual(expected, actual)

        expected = [['ï»¿X', 'Y'], ['0', '0'], ['1', '20'], ['2', '30'], ['3', '100'], ['4', '160'], ['5', '200'],
                    ['6', '160'], ['7', '90'], ['8', '70'], ['9', '30'], ['10', '10']]
        actual = csv_functions.csv_open('test_2.csv')
        self.assertEqual(expected, actual)
