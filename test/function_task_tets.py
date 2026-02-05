import unittest
from src import function_task

class TestConvertMinutesFunction(unittest.TestCase):
    def test_that_convert_minutes_function_exist(self):
        function_task.convert_minutes(130)

    def test_that_convert_minutes_function_return_time_with_minutes_arguments(self):
        actual = function_task.convert_minutes(130)
        expected = "130 minutes is 2 hours 10 minutes"
        self.assertEqual(actual,expected)

    def test_that_get_multiplication_function_exist(self):
        function_task.get_multiplication(3, 2)

    def test_that_get_multiplication_function_return_number_one_number_two_arguments(self):
        actual = function_task.get_multiplication(3, 2)
        expected = 6
        self.assertEqual(actual, expected)
