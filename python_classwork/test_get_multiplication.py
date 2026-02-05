import unittest
import function_task

class TestGetMultiplicationFunction(unittest.TestCase):
    def test_that_get_multiplication_function_exist(self):
        function_task.get_multiplication(3, 2)

    def test_that_get_multiplication_function_return_number_one_number_two_arguments(self):
        actual = function_task.get_multiplication(3, 2)
        expected = 6
        self.assertEqual(actual,expected)
