import unittest
import function

class TestFunction(unittest.TestCase):
    def test_that_check_list_function_exist(self):
        function.check_list()

    def test_that_check_list_function_return_one_to_fifteen(self):
        actual = function.check_list()
        expected = list(range(1, 16))
        self.assertEqual(actual,expected)


    def test_that_add_third_element_function_exist(self):
        function.add_third_element([1,2,3,4,5,6,7,8,9])

    def test_that_add_third_element_function_returns_total_of_count(self):
        actual = function.add_third_element([1,2,3,4,5,6,7,8,9])
        expected = 3 + 6 + 9
        self.assertEqual(actual,expected)



    def test_that_sum_first_middle_last_function_exist(self):
        function.sum_first_middle_last([2,4,5,7,6])

    def test_that_add_third_element_function_returns_total_of_count(self):
        actual = function.sum_first_middle_last([2, 4,5,7,6])
        expected = 2 + 5 + 6
        self.assertEqual(actual,expected)
