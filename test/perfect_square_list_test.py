import unittest

from perfect_square_array import sum_up_rows


class TestPerfectSquareArray(unittest.TestCase):
    def test_that_rows_and_columns_are_perfect_squares(self):
        list_of_numbers = [
            [5, 4, 1],
            [2, 6, 2],
            [3, 0, 7]
        ]
        self.assertTrue(sum_up_rows(list_of_numbers))

    def test_that_rows_and_columns_are_not_perfect_squares(self):
        list_of_numbers = [
            [5, 4, 1],
            [2, 6, 2],
            [4, 0, 7]
        ]
        self.assertFalse(sum_up_rows(list_of_numbers))
    #
    def test_that_rows_and_columns_are_perfect_for_2D(self):
        list_of_numbers = [
            [2, 3],
            [3, 2]
        ]
        self.assertTrue(sum_up_rows(list_of_numbers))

    def test_that_rows_and_columns_are_not_perfect_for_2D(self):
        list_of_numbers = [
            [2, 3],
            [4, 2]
        ]
        self.assertFalse(sum_up_rows(list_of_numbers))

    def test_that_rows_and_columns_are_empty(self):
        list_of_numbers = []
        self.assertFalse(sum_up_rows(list_of_numbers))

    def test_that_rows_and_columns_have_one_list(self):
        list_of_numbers = [
            [5, 4, 1],
        ]
        self.assertTrue(sum_up_rows(list_of_numbers))